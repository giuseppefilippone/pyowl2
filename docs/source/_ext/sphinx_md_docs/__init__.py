"""
sphinx_md_docs — Sphinx Extension
=======================================
Injects LLM-generated Markdown descriptions (produced by ``code_documenter.py``)
into Sphinx-AutoAPI pages at build time.

Instead of post-processing RST files on disk, this extension hooks into the
Sphinx ``source-read`` event so that descriptions are injected *in memory*
while Sphinx processes each page.  It works with or without
``autoapi_keep_files``.

Setup
-----
In your ``conf.py``:

.. code-block:: python

    extensions = [
        "autoapi.extension",
        "sphinx_md_docs",       # ← this extension
    ]

    autoapi_dirs = ["../src"]

    # Path to the directory that code_documenter.py wrote.
    # Absolute, or relative to conf.py's directory (srcdir).
    sphinx_md_injector_dir = "md"

    # (Optional) override the autoapi root if you changed it.
    # Defaults to the value of ``autoapi_root`` (which defaults to "autoapi").
    # sphinx_md_injector_autoapi_root = "autoapi"

How it works
------------
1. On ``builder-inited`` (priority 900, well after AutoAPI's default 500),
   the extension scans ``sphinx_md_injector_dir`` and builds a lookup table that
   maps dotted module names to their Markdown content.

2. On every ``source-read`` event, if the docname lives under the AutoAPI
   root (e.g. ``autoapi/pkg/sub/module/index``), the extension:

   a. Derives the dotted module name from the path.
   b. Looks up the matching Markdown.
   c. Converts the Markdown to RST.
   d. Injects the RST block into the source before Sphinx parses it.
"""

from __future__ import annotations

import re
from logging import DEBUG
from pathlib import Path
from typing import TYPE_CHECKING, Any

from sphinx.util import logging

if TYPE_CHECKING:
    from sphinx.application import Sphinx

__version__ = "1.0.0"

logger = logging.getLogger(__name__)
logger.setLevel(DEBUG)

logger.debug(
    "[md_docs] Sphinx MD Docs extension loaded (name =%s, version=%s)",
    __name__,
    __version__,
)

# ──────────────────────────────────────────────
# CONSTANTS & CONFIG
# ──────────────────────────────────────────────

LLM_MODEL = "glm-4.7:cloud"

# ──────────────────────────────────────────────
# Markdown → RST converter
# ──────────────────────────────────────────────

_RST_HEADING_CHARS = ["=", "-", "~", "^", '"']


def _md_to_rst(md_text: str) -> str:
    """Convert the Markdown subset produced by code_documenter.py to RST."""
    lines = md_text.splitlines()
    rst: list[str] = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # ── Fenced code block ──
        if line.strip().startswith("```"):
            lang = line.strip().lstrip("`").strip()
            rst.append("")
            rst.append(f".. code-block:: {lang}" if lang else ".. code-block::")
            rst.append("")
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                rst.append(f"   {lines[i]}")
                i += 1
            rst.append("")
            i += 1
            continue

        # ── Headings ──
        m = re.match(r"^(#{1,5})\s+(.+)$", line)
        if m:
            level = len(m.group(1)) - 1
            title = _convert_inline(m.group(2))
            char = _RST_HEADING_CHARS[min(level, len(_RST_HEADING_CHARS) - 1)]
            rst.append("")
            rst.append(title)
            rst.append(char * len(title))
            rst.append("")
            i += 1
            continue

        # ── Blockquote ──
        if line.startswith("> "):
            quote: list[str] = []
            while i < len(lines) and lines[i].startswith("> "):
                quote.append(lines[i][2:])
                i += 1
            rst.append("")
            for ql in quote:
                rst.append(f"   {_convert_inline(ql)}")
            rst.append("")
            continue

        # ── Unordered list ──
        lm = re.match(r"^(\s*)[-*]\s+(.+)$", line)
        if lm:
            rst.append(f"{lm.group(1)}* {_convert_inline(lm.group(2))}")
            i += 1
            continue

        # Check for block math in the same line (e.g. "Here is $$x^2$$ inline")
        if "$$" in line:
            rst.append(_convert_mathjax(line))
            i += 1
            continue

        if "$" in line:
            rst.append(_convert_math_inline(line))
            i += 1
            continue

        # ── Regular line ──
        rst.append(_convert_inline(line))
        i += 1

    return "\n".join(rst)


def _convert_math_inline(text: str) -> str:
    """Convert inline math from Markdown ($...$) to RST (:math:`...`)."""
    return re.sub(r"\$(.+?)\$", r":math:`\1`", text)


def _convert_mathjax(text: str) -> str:
    """Convert math blocks from Markdown ($$...$$) to RST math directives."""

    def replacer(match: re.Match) -> str:
        content = match.group(1)
        lines = content.splitlines()
        return "\n.. math::\n\n" + "\n".join(f"   {line}" for line in lines) + "\n"

    return re.sub(r"\$\$(.+?)\$\$", replacer, text, flags=re.DOTALL)


def _convert_inline(text: str) -> str:
    """Convert inline Markdown to RST."""
    # [text](url) → `text`_
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"`\1`", text)
    # `code` → ``code`` (avoid already-double backticks)
    text = re.sub(r"(?<!`)(`)((?!`)[^`]+)(`)((?!`))", r"``\2``", text)
    return text


# ──────────────────────────────────────────────
# Strip the MD header (title + file line)
# ──────────────────────────────────────────────


def _strip_md_header(md_text: str) -> str:
    """Remove the ``# module_name`` heading and ``**File:**`` line that
    ``code_documenter.py`` puts at the top — AutoAPI already shows those."""
    lines = md_text.splitlines()
    out: list[str] = []
    skip = True
    for line in lines:
        if skip:
            if (
                line.startswith("# ")
                or line.startswith("**File:**")
                or not line.strip()
            ):
                continue
            skip = False
        out.append(line)
    return "\n".join(out)


# ──────────────────────────────────────────────
# Markdown file discovery
# ──────────────────────────────────────────────


def _build_md_lookup(md_dir: Path) -> dict[str, str]:
    """Scan ``md_dir`` and return ``{dotted_name: rst_content}``."""
    lookup: dict[str, str] = {}

    for md_file in sorted(md_dir.glob("*.md")):
        logger.debug("[md_injector] Processing Markdown file: %s", md_file)

        stem = md_file.stem

        if stem == "INDEX":
            key = "__ROOT__"
        else:
            key = stem

        raw_md = md_file.read_text(encoding="utf-8")
        stripped = _strip_md_header(raw_md)
        rst = _md_to_rst(stripped)

        if rst.strip():
            lookup[key] = rst
            logger.debug("[md_injector] Loaded: %s → %s", md_file.name, key)

    return lookup


# ──────────────────────────────────────────────
# Injection into RST source
# ──────────────────────────────────────────────

_INJECT_START = ".. ── LLM-GENERATED DESCRIPTION START ──"
_INJECT_END = ".. ── LLM-GENERATED DESCRIPTION END ──"

# Section headings that AutoAPI generates — we inject *before* the first one.
_SECTION_MARKERS = {
    "Subpackages",
    "Submodules",
    "Module Contents",
    "Package Contents",
    "Attributes",
    "Classes",
    "Functions",
    "Exceptions",
}

_UNDERLINE_RE = re.compile(r"^([=\-~^\"]{3,})\s*$")


def _find_injection_point(lines: list[str]) -> int:
    """Return the line index where description should be inserted."""
    # 1) Before the first known AutoAPI content section
    for i, line in enumerate(lines):
        if line.strip() in _SECTION_MARKERS:
            if i + 1 < len(lines) and _UNDERLINE_RE.match(lines[i + 1].strip()):
                return i

    # 2) Before the first toctree directive
    for i, line in enumerate(lines):
        if ".. toctree::" in line:
            return i

    # 3) Append at the end
    return len(lines)


def _inject(source_rst: str, description_rst: str) -> str:
    """Inject or replace the description block inside an RST source string."""
    lines = source_rst.splitlines()

    # Remove previous injection if present
    start_idx = end_idx = None
    for i, line in enumerate(lines):
        if line.strip() == _INJECT_START:
            start_idx = i
        elif line.strip() == _INJECT_END:
            end_idx = i
            break
    if start_idx is not None and end_idx is not None:
        lines = lines[:start_idx] + lines[end_idx + 1 :]

    # Find the right place
    point = _find_injection_point(lines)

    block = [
        "",
        _INJECT_START,
        "",
        description_rst,
        "",
        _INJECT_END,
        "",
    ]

    lines = lines[:point] + block + lines[point:]
    return "\n".join(lines)


# ──────────────────────────────────────────────
# Sphinx event callbacks
# ──────────────────────────────────────────────


def _on_builder_inited(app: Sphinx) -> None:
    """Load all Markdown files into memory once at build start."""
    logger.info("[md_injector] Markdown injector initializing...")

    md_dir_cfg = app.config.sphinx_md_injector_dir
    logger.debug(
        "[md_injector] Initializing with sphinx_md_injector_dir: %s", md_dir_cfg
    )
    if not md_dir_cfg:
        logger.warning("[md_injector] sphinx_md_injector_dir is not set — skipping")
        return

    md_dir = Path(md_dir_cfg)
    if not md_dir.is_absolute():
        md_dir = Path(app.confdir) / md_dir

    if app.config.sphinx_md_injector_generate:
        logger.debug(
            "[md_injector] Starting to process library for Markdown generation..."
        )
        # Lazy import — langchain is only needed here
        from .code_docs import process_library  # noqa: F811

        process_library(
            md_dir,
            Path((Path(app.confdir) / app.config.autoapi_dirs[0]).resolve()),
            LLM_MODEL,
        )
        logger.debug("[md_injector] Finished processing library.")

    if not md_dir.is_dir():
        logger.error("[md_injector] Markdown directory does not exist: %s", md_dir)
        return

    lookup = _build_md_lookup(md_dir)
    logger.debug("[md_injector] Loaded %d description(s) from %s", len(lookup), md_dir)

    autoapi_root = getattr(app.config, "sphinx_md_injector_autoapi_root", None)
    if autoapi_root is None:
        autoapi_root = getattr(app.config, "autoapi_root", "autoapi")
    autoapi_root = Path(app.srcdir) / autoapi_root  # ensure consistent path style
    if not autoapi_root.is_dir():
        logger.error(
            "[md_injector] AutoAPI root directory does not exist: %s", autoapi_root
        )
        return

    logger.debug("[md_injector] Using AutoAPI root: %s", autoapi_root)

    for key in lookup:
        logger.debug("[md_injector] Available description key: %s", key)
        if key == "__ROOT__":
            source_path = autoapi_root / "index.rst"
        else:
            if key.endswith("_INDEX"):
                source_path = (
                    autoapi_root
                    / Path(*key.replace("_INDEX", "").split("."))
                    / "index.rst"
                )
            else:
                source_path = autoapi_root / Path(*key.split(".")) / "index.rst"

        logger.debug("[md_injector] → would inject into: %s", source_path.as_posix())

        source = _inject(source_path.read_text(encoding="utf-8"), lookup[key])
        logger.debug(
            "[md_injector] ✓ Injected description into %s", source_path.as_posix()
        )
        source_path.write_text(source, encoding="utf-8")
    logger.info("[md_injector] Completed injecting descriptions.")


# ──────────────────────────────────────────────
# Extension entry point
# ──────────────────────────────────────────────


def setup(app: Sphinx) -> dict[str, Any]:
    """Register the extension with Sphinx."""

    logger.debug("[md_docs] Setting up Sphinx MD Docs extension")

    # Config values
    app.add_config_value("sphinx_md_injector_dir", default="", rebuild="env")
    app.add_config_value("sphinx_md_injector_generate", default=False, rebuild="env")
    app.add_config_value("sphinx_md_injector_autoapi_root", default=None, rebuild="env")

    # Events
    logger.debug("[md_injector] Connecting Sphinx events")
    app.connect("builder-inited", _on_builder_inited)

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
