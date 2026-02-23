"""
sphinx_uml_autodoc — UML class diagrams for sphinx-autoapi & autodoc
====================================================================

Architecture
~~~~~~~~~~~~

Everything happens in ``builder-inited``, which fires once before Sphinx
reads any RST.  Because this extension is listed **after** autoapi in
the ``extensions`` list, autoapi has already written its RST files to
``{srcdir}/{autoapi_root}/`` by the time this handler runs.

Step 1 — Generate PNGs:
    Walk ``autoapi_dirs`` source trees via ``ast.parse`` (no import
    needed) and render a UML diagram for each class.

Step 2 — Patch autoapi RST on disk:
    Walk every ``.rst`` file under ``{srcdir}/{autoapi_root}/``, find
    ``.. py:class::`` directives, and insert a ``.. figure::``
    directive pointing to the pre-generated PNG immediately before
    each one.

This is the only reliable injection point for autoapi — the
``source-read`` and ``autodoc-process-docstring`` events do not
reliably fire for autoapi-generated content.

A fallback ``autodoc-process-docstring`` handler is also registered
for users of plain ``sphinx.ext.autodoc`` (no autoapi).
"""

from __future__ import annotations

import ast
import hashlib
import importlib
import inspect
import os
import re
import subprocess
import tempfile
from glob import glob
from logging import DEBUG
from pathlib import Path
from typing import TYPE_CHECKING, Any, Optional, Type

from sphinx.util import logging

if TYPE_CHECKING:
    from sphinx.application import Sphinx
    from sphinx.config import Config

__version__ = "6.0.0"
logger = logging.getLogger(__name__)
logger.setLevel(DEBUG)

# ─── configuration defaults ───────────────────────────────────────────
_DEFAULTS: dict[str, Any] = {
    "uml_dpi": 150,  # PNG resolution (DPI)
    "uml_output_dir": "_uml",  # image dir (relative to docs srcdir)
    "uml_font_name": "Sans",  # Graphviz font family (e.g. "Sans", "Helvetica", "Times")
    "uml_font_size": 12,  # base font size (pt) — Graphviz scales all other fonts proportionally
    "uml_max_inheritance_depth": 1,  # ancestor levels (pyreverse -a)
    "uml_association_depth": 0,  # associated-class depth (pyreverse -s)
    "uml_show_private": False,  # include _private members
    "uml_rankdir": "LR",  # graph direction: TB | BT | LR | RL
    "uml_backend": "auto",  # "pyreverse" | "inspect" | "auto"
}

# A4 text area with Sphinx's default LaTeX margins.
_MAX_TEXT_WIDTH_CM = 15.0
_MAX_TEXT_HEIGHT_CM = 20.0  # ~22 cm minus caption + float spacing
_LANDSCAPE_MIN_RATIO = 2.5  # only consider landscape if width ≥ 2.5× height
_LANDSCAPE_GAIN = 0.20  # AND landscape must give ≥ 20% larger image

_SKIP = frozenset(
    {
        "__annotations__",
        "__dict__",
        "__doc__",
        "__module__",
        "__weakref__",
        "__slots__",
        "__abstractmethods__",
        "_abc_impl",
        "__class__",
        "__delattr__",
        "__dir__",
        "__format__",
        "__getattribute__",
        "__gt__",
        "__hash__",
        "__reduce__",
        "__reduce_ex__",
        "__setattr__",
        "__sizeof__",
        "__subclasshook__",
        "__init_subclass__",
    }
)

# ─── colour palette ──────────────────────────────────────────────────
_P = {
    "header_bg": "#4A90D9",
    "header_fg": "#FFFFFF",
    "section_bg": "#EAF2FB",
    "border": "#2C6FAC",
    "assoc_header_bg": "#7B7B7B",
    "assoc_section_bg": "#F0F0F0",
    "assoc_border": "#555555",
    "edge_inherit": "#2C6FAC",
    "edge_assoc": "#888888",
}


# =====================================================================
#  builder-inited — the only hook that matters for autoapi
# =====================================================================


def _new_lines(conf: Config, uml_dir: Path, safe: str, short: str):
    new_lines: list[str] = []
    # Relative path from srcdir for the figure directive
    png_rel = f"/{conf.uml_output_dir}/{safe}.png"
    pdf_rel = f"/{conf.uml_output_dir}/{safe}.pdf"
    png_abs = uml_dir / f"{safe}.png"
    w, h = _image_dimensions(png_abs)
    landscape = _should_landscape(w, h, conf.uml_dpi)
    latex_width = _latex_width(w, h, conf.uml_dpi, landscape)

    try:
        from PIL import Image

        with Image.open(png_abs).convert("RGBA") as img:
            alpha = img.getchannel("A")
            # if image is fully transparent -> skip it
            if alpha.getextrema() == (0, 0):
                logger.info(f"[uml] Skipping empty figure -> {safe}")
                return new_lines
    except ImportError:
        pass

    # ── HTML ────────────────────────────────────────────────────────
    new_lines.append(".. only:: html\n")

    new_lines.append(f"    .. figure:: {png_rel}")
    new_lines.append(f"       :alt: UML Class Diagram for {short}")
    new_lines.append("       :align: center")
    new_lines.append("       :width: 100%")
    new_lines.append("       :class: uml-diagram")
    new_lines.append("")
    new_lines.append(f"       UML Class Diagram for **{short}**")
    new_lines.append("")

    # ── LaTeX / PDF ─────────────────────────────────────────────────
    new_lines.append(".. only:: latex\n")

    if landscape:
        new_lines.append("    .. raw:: latex\n")
        new_lines.append(r"       \begin{landscape}" + "\n")
        new_lines.append(r"       \vspace*{\fill}" + "\n")

    new_lines.append(f"    .. figure:: {pdf_rel}")
    new_lines.append(f"       :alt: UML Class Diagram for {short}")
    new_lines.append("       :align: center")
    new_lines.append(f"       :width: {latex_width}")
    new_lines.append("       :class: uml-diagram\n")
    new_lines.append(f"       UML Class Diagram for **{short}**\n")

    if landscape:
        new_lines.append("    .. raw:: latex\n")
        new_lines.append(r"       \vspace*{\fill}" + "\n")
        new_lines.append(r"       \end{landscape}" + "\n")

    return new_lines


def _on_builder_inited(app: Sphinx) -> None:
    conf = app.config
    src_dir = Path(app.srcdir)
    uml_dir = src_dir / conf.uml_output_dir
    uml_dir.mkdir(parents=True, exist_ok=True)

    # ── discover source roots ───────────────────────────────────────
    autoapi_dirs: list[str] = getattr(conf, "autoapi_dirs", [])
    roots: list[Path] = []
    for d in autoapi_dirs:
        p = Path(d)
        if not p.is_absolute():
            p = (Path(app.confdir) / d).resolve()
        if p.is_dir():
            roots.append(p)

    if not roots:
        logger.info(
            "[uml] No autoapi_dirs configured — " "will use autodoc fallback only."
        )
        return

    # ── Step 1: AST-scan for classes and generate PNGs ──────────────
    classes: list[tuple[str, str]] = []  # (fqn, source_path)
    modules: list[tuple[str, str]] = []
    for root in roots:
        for py in sorted(root.rglob("*.py")):
            rel = py.relative_to(root.parent)
            parts = list(rel.with_suffix("").parts)
            if parts[-1] == "__init__":
                mod_fqn = ".".join(parts[:-1]) if len(parts) > 1 else parts[0]
            else:
                mod_fqn = ".".join(parts)
            try:
                tree = ast.parse(py.read_text(encoding="utf-8"), str(py))
            except SyntaxError:
                continue
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    classes.append((f"{mod_fqn}.{node.name}", str(py)))
                elif isinstance(node, ast.Module) and str(py).endswith("__init__.py"):
                    modules.append((mod_fqn, str(py).replace("/__init__.py", "")))

    logger.info(
        "[uml] Found %d classes across %d source dir(s).", len(classes), len(roots)
    )
    logger.info(
        "[uml] Found %d modules across %d source dir(s).", len(modules), len(roots)
    )

    use_pyreverse = conf.uml_backend != "inspect" and _pyreverse_ok()
    generated: set[str] = set()  # FQNs with successful PNGs

    for fqn, src_file in classes:
        safe = "class_" + fqn.replace(".", "_")
        base = uml_dir / safe
        ok = os.path.exists(str(base) + ".pdf")  # False

        logger.info("[uml] Processing %s from %s ...", fqn, src_file)

        if not ok and use_pyreverse:
            ok = _pyreverse_class(fqn, src_file, base, app)

        assert ok

        # if not ok:
        #     cls = _try_import(fqn)
        #     if cls is not None:
        #         try:
        #             dot = _inspect_dot(cls, conf)
        #             _render_vector(dot, base)
        #             ok = True
        #         except Exception as exc:
        #             logger.info("[uml] inspect fallback failed for %s: %s", fqn, exc)

        if ok:
            generated.add(fqn)

    logger.info(
        "[uml] Generated %d / %d PNG diagrams for the classes.",
        len(generated),
        len(classes),
    )

    generated.clear()
    for fqn, src_file in modules:
        safe = "module_" + fqn.replace(".", "_")
        base = uml_dir / safe
        ok = os.path.exists(str(base) + ".pdf")  # False

        logger.info("[uml] Processing %s from %s ...", fqn, src_file)

        if not ok and use_pyreverse:
            ok = _pyreverse_class(fqn, src_file, base, app, module=True)

        assert ok

        # if not ok:
        #     cls = _try_import(fqn)
        #     if cls is not None:
        #         try:
        #             dot = _inspect_dot(cls, conf)
        #             _render_vector(dot, base)
        #             ok = True
        #         except Exception as exc:
        #             logger.debug("[uml] inspect fallback failed for %s: %s", fqn, exc)

        if ok:
            generated.add(fqn)

    logger.info(
        "[uml] Generated %d / %d PNG diagrams for the modules.",
        len(generated),
        len(modules),
    )

    # ── Step 2: Patch autoapi RST files on disk ─────────────────────
    autoapi_root: str = getattr(conf, "autoapi_root", "autoapi")
    rst_dir = src_dir / autoapi_root

    if not rst_dir.is_dir():
        logger.warning(
            "[uml] autoapi RST dir not found: %s "
            "(autoapi may not have run yet — ensure "
            "'sphinx_uml_autodoc' is listed AFTER "
            "'autoapi.extension' in conf.py extensions)",
            rst_dir,
        )
        return

    patched_files = 0
    patched_classes = 0
    seen = set()

    for rst_file in sorted(rst_dir.rglob("*.rst")):
        text = rst_file.read_text(encoding="utf-8")

        # Extract module name from  .. py:module:: <fqn>
        mod_m = re.search(r"^\.\.\s+py:module::\s+(\S+)", text, re.MULTILINE)

        if not mod_m:
            continue

        module_fqn = mod_m.group(1)

        # Find all  .. py:class:: ClassName  lines
        # The class name might be followed by (args) on the same line.
        lines = text.split("\n")
        new_lines: list[str] = []
        n_injected = 0

        for line in lines:
            cls_m = re.match(
                r"^(\.\.\s+py:class::\s+)(\w+)",
                line,
            )
            module_m = re.match(
                r"^(\.\.\s+py:module::\s+)(.*)",
                line,
            )
            if cls_m and "figure::" not in text:
                class_short = cls_m.group(2)
                fqn = f"{module_fqn}.{class_short}"
                safe = "class_" + fqn.replace(".", "_")
                png_path: Path = uml_dir / f"{safe}.png"
                pdf_path: Path = uml_dir / f"{safe}.pdf"

                if not png_path.exists() or png_path in seen:
                    continue
                if not pdf_path.exists() or pdf_path in seen:
                    continue

                seen.add(png_path)
                seen.add(pdf_path)

                new_lines.extend(_new_lines(conf, uml_dir, safe, class_short))

                # w, _ = _image_dimensions(png_path)
                # landscape = w > conf.uml_landscape_threshold
                # # Relative path from srcdir for the figure directive
                # png_rel = f"/{conf.uml_output_dir}/{safe}.png"

                # new_lines.append("")

                # if landscape:
                #     new_lines.append(".. raw:: latex")
                #     new_lines.append("")
                #     new_lines.append(r"   \begin{landscape}")
                #     new_lines.append("")

                # new_lines.append(f".. figure:: {png_rel}")
                # new_lines.append(f"   :alt: UML Class Diagram for {class_short}")
                # new_lines.append("   :align: center")
                # new_lines.append("   :width: 70%")
                # new_lines.append("")
                # new_lines.append(f"   UML Class Diagram for **{class_short}**")
                # new_lines.append("")

                # if landscape:
                #     new_lines.append(".. raw:: latex")
                #     new_lines.append("")
                #     new_lines.append(r"   \end{landscape}")
                #     new_lines.append("")

                n_injected += 1

            if module_m and "py:class" not in text and "figure::" not in text:
                fqn = module_fqn
                safe = "module_" + fqn.replace(".", "_")
                png_path: Path = uml_dir / f"{safe}.png"
                pdf_path: Path = uml_dir / f"{safe}.pdf"

                if not png_path.exists() or png_path in seen:
                    continue
                if not pdf_path.exists() or pdf_path in seen:
                    continue

                seen.add(pdf_path)
                seen.add(png_path)

                new_lines.extend(_new_lines(conf, uml_dir, safe, module_fqn))

                n_injected += 1

            new_lines.append(line)

        if n_injected > 0:
            rst_file.write_text("\n".join(new_lines), encoding="utf-8")
            patched_files += 1
            patched_classes += n_injected
            logger.debug(
                "[uml] Patched %s: injected %d diagram(s)", rst_file.name, n_injected
            )

    logger.info(
        "[uml] Patched %d RST file(s), injected %d diagram(s).",
        patched_files,
        patched_classes,
    )

    removed: int = 0
    for dot in glob(f"{uml_dir}/**.dot"):
        os.remove(dot)
        removed += 1

    logger.info(f"[uml] Removed {removed} dot files.")


# =====================================================================
#  Vector rendering: DOT → SVG + PDF
# =====================================================================


def _render_vector(dot_source: str, base_path: Path) -> None:
    """
    Render DOT source to ``base_path.png`` and ``base_path.pdf``.
    Both are vector — tiny files, instant LaTeX compilation.
    """
    base_path.parent.mkdir(parents=True, exist_ok=True)
    dot_file = base_path.with_suffix(".dot")
    dot_file.write_text(dot_source, encoding="utf-8")

    for fmt in ("png", "pdf"):
        out = base_path.with_suffix(f".{fmt}")
        try:
            subprocess.run(
                ["dot", f"-T{fmt}", "-o", str(out), str(dot_file)],
                check=True,
                capture_output=True,
                text=True,
            )
        except FileNotFoundError:
            raise RuntimeError("Graphviz 'dot' not found")
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Graphviz ({fmt}): {e.stderr}") from e

        if fmt == "pdf":
            _fix_pdf(out)


def _image_dimensions(p: Path) -> tuple[int, int]:
    try:
        from PIL import Image

        Image.MAX_IMAGE_PIXELS = 1 << 30  # ~1 gigapixel, just in case
        with Image.open(p) as im:
            return im.size
    except ImportError:
        pass

    with open(p, "rb") as f:
        d = f.read(32)
    if d[:8] != b"\x89PNG\r\n\x1a\n":
        return 800, 600
    import struct

    return struct.unpack(">II", d[16:24])


# =====================================================================
#  pyreverse backend
# =====================================================================


def _pyreverse_ok() -> bool:
    try:
        subprocess.run(["pyreverse", "--help"], capture_output=True, timeout=10)
        return True
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return False


def _pyreverse_class(
    fqn: str, source_file: str, output_path: Path, app: Sphinx, module: bool = False
) -> bool:
    conf: Config = app.config
    class_name = fqn.rsplit(".", 1)[-1]

    logger.info("[uml] Attempting to generate diagram for %s using pyreverse ...", fqn)
    logger.info(
        "[uml] Running pyreverse on %s with class focus '%s' ...",
        source_file,
        class_name,
    )

    with tempfile.TemporaryDirectory(prefix="uml_") as tmpdir:
        if not module:
            cmd = [
                "pyreverse",
                "--verbose",
                "-mn",
                "-o",
                "dot",
                "-c",
                class_name,
                f"-a {conf.uml_max_inheritance_depth}",
                f"-s {conf.uml_association_depth}",
                "--filter-mode=ALL",
                # "--colorized",
                source_file,
            ]
        else:
            cmd = [
                "pyreverse",
                "--verbose",
                "-o",
                "dot",
                # "-p",
                # fqn,
                # fqn.replace(".", "_"),
                "-a",
                "1",
                source_file,
            ]

        env = os.environ.copy()
        extra = []
        for d in getattr(conf, "autoapi_dirs", []):
            p = Path(d)
            if not p.is_absolute():
                p = (Path(app.confdir) / d).resolve()
            par = str(p.parent)
            if par not in extra:
                extra.append(par)
        if extra:
            env["PYTHONPATH"] = (
                os.pathsep.join(extra) + os.pathsep + env.get("PYTHONPATH", "")
            )

        try:
            logger.info("[uml] PYTHONPATH for pyreverse: %s", env.get("PYTHONPATH", ""))
            logger.info("[uml] Running command: %s", " ".join(cmd))
            r = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                cwd=tmpdir,
                timeout=30,  # env=env
            )
            if r.returncode != 0:
                logger.error("[uml] pyreverse failed for %s: %s", fqn, r.stderr)
                return False
        except (FileNotFoundError, subprocess.TimeoutExpired) as exc:
            logger.error("[uml] pyreverse failed for %s: %s", fqn, exc)
            return False

        dots = list(Path(tmpdir).glob("./*.dot"))
        if not dots:
            logger.error("[uml] pyreverse failed for %s: no dot files generated", fqn)
            return False

        styled = _postprocess_dot(
            dots[0].read_text(encoding="utf-8"),
            class_name if not module else fqn.replace(".", "_"),
            font_name=conf.uml_font_name,
            font_size=conf.uml_font_size,
            rankdir=conf.uml_rankdir if module else "TB",
            dpi=conf.uml_dpi,
        )

        try:
            _render_vector(styled, output_path)
            return True
        except RuntimeError as exc:
            logger.error("[uml] pyreverse failed for %s: %s", fqn, exc)
            return False


# =====================================================================
#  DOT post-processing (pyreverse → styled UML)
# =====================================================================


def _postprocess_dot(
    dot: str,
    focus: str,
    *,
    font_name: str,
    font_size: int,
    rankdir: str,
    dpi: int,
) -> str:
    g = (
        f"    graph [dpi={dpi}, rankdir={rankdir}, bgcolor=transparent, "
        f'fontname="{font_name}", pad=0, margin=0.1];\n'
        f'    node  [fontname="{font_name}", fontsize={font_size}];\n'
        f'    edge  [fontname="{font_name}", fontsize={font_size - 1}];\n'
    )
    # br = dot.index("{")
    # dot = dot[: br + 1] + "\n" + g + dot[br + 1 :]
    dot = dot.splitlines(keepends=True)
    dot[1:3] = g.splitlines(keepends=True)

    return "".join(dot)

    node_re = re.compile(
        r'^\s*(?P<n>"[^"]+"|[\w]+)\s*\[label\s*=\s*"(?P<l>\{[^"]*\})"'
        r"(?P<r>[^\]]*)\];",
        re.MULTILINE,
    )

    def _conv(m: re.Match) -> str:
        nid, lb, rest = m.group("n").strip(), m.group("l"), m.group("r")
        inner = lb.strip().strip("{}")
        pts = inner.split("|")
        title = pts[0].replace("\\l", "").strip()
        at = pts[1].strip() if len(pts) > 1 else ""
        me = pts[2].strip() if len(pts) > 2 else ""
        is_f = title == focus or title == focus.split(".")[-1]
        hbg = _P["header_bg"] if is_f else _P["assoc_header_bg"]
        sbg = _P["section_bg"] if is_f else _P["assoc_section_bg"]
        bc = _P["border"] if is_f else _P["assoc_border"]
        pw = "2" if is_f else "1"

        def _r(raw: str) -> str:
            ls = [l.strip() for l in raw.replace("\\l", "\n").split("\n") if l.strip()]
            if not ls:
                return "<TR><TD> </TD></TR>"
            return "".join(
                f'<TR><TD ALIGN="LEFT" BALIGN="LEFT">{_esc(l)}</TD></TR>' for l in ls
            )

        h = (
            f'<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" '
            f'CELLPADDING="4" COLOR="{bc}">'
            f'<TR><TD BGCOLOR="{hbg}"><FONT COLOR="{_P["header_fg"]}"><B>'
            f"{_esc(title)}</B></FONT></TD></TR>"
            f'<TR><TD><TABLE BORDER="0" CELLSPACING="0" CELLPADDING="2"'
            f' BGCOLOR="{sbg}">{_r(at)}</TABLE></TD></TR>'
            f'<TR><TD><TABLE BORDER="0" CELLSPACING="0" CELLPADDING="2"'
            f' BGCOLOR="{sbg}">{_r(me)}</TABLE></TD></TR>'
            f"</TABLE>>"
        )
        rest = re.sub(r',?\s*shape\s*=\s*"[^"]*"', "", rest)
        return f"    {nid} [label={h}, shape=plaintext, penwidth={pw}{rest}];"

    dot = node_re.sub(_conv, dot)
    dot = re.sub(
        r'arrowhead\s*=\s*"empty"',
        f'arrowhead="empty", color="{_P["edge_inherit"]}"',
        dot,
    )
    dot = re.sub(
        r'arrowhead\s*=\s*"diamond"',
        f'arrowhead="diamond", color="{_P["edge_assoc"]}", ' f'style="bold"',
        dot,
    )
    for a in ("open", "normal"):
        dot = re.sub(
            rf'arrowhead\s*=\s*"{a}"',
            f'arrowhead="{a}", color="{_P["edge_assoc"]}"',
            dot,
        )
    return dot


def _esc(t: str) -> str:
    return (
        t.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


# =====================================================================
#  inspect fallback backend
# =====================================================================


# def _pub(n: str, priv: bool) -> bool:
#     if n in _SKIP:
#         return False
#     if n.startswith("__") and n.endswith("__"):
#         return True
#     return priv or not n.startswith("_")


# def _members(cls: Type, priv: bool) -> tuple[list[str], list[str]]:
#     import typing as _t

#     attrs: list[str] = []
#     meths: list[str] = []
#     try:
#         ann = _t.get_type_hints(cls)
#     except Exception:
#         ann = {}
#         for k in reversed(cls.__mro__):
#             ann.update(getattr(k, "__annotations__", {}))
#     for an, at in ann.items():
#         if not _pub(an, priv):
#             continue
#         ts = at.__name__ if isinstance(at, type) else str(at).replace("typing.", "")
#         ts = re.sub(r"[\w]+\.(?=[A-Z])", "", ts)
#         attrs.append(f"{an}: {ts}")

#     seen = {a.split(":")[0].strip() for a in attrs}
#     for nm in sorted(vars(cls)):
#         if not _pub(nm, priv):
#             continue
#         v = vars(cls)[nm]
#         if isinstance(v, (staticmethod, classmethod)):
#             fn = v.__func__ if hasattr(v, "__func__") else v
#             pfx = "«static» " if isinstance(v, staticmethod) else "«class» "
#             meths.append(f"{pfx}{nm}{_sig(fn)}")
#         elif callable(v) and not isinstance(v, type):
#             meths.append(f"{nm}{_sig(v)}")
#         elif isinstance(v, property):
#             r = ""
#             if v.fget and v.fget.__annotations__.get("return"):
#                 rv = v.fget.__annotations__["return"]
#                 r = f": {rv.__name__ if isinstance(rv, type) else str(rv)}"
#             attrs.append(f"«property» {nm}{r}")
#         elif nm not in seen:
#             attrs.append(nm)
#     return attrs, meths


def _pub(n: str) -> bool:
    """Keep every member except internal noise (``_SKIP``)."""
    return n not in _SKIP


def _members(cls: Type) -> tuple[list[str], list[str]]:
    """
    Collect the class's **own** attributes and methods.

    Attributes come from ``cls.__annotations__`` (own only — not the
    MRO-wide ``get_type_hints``), so inherited annotations are excluded.
    Methods come from ``vars(cls)`` which is own-only by definition.
    Private members (single ``_``) are always included; UML marks
    them with a visibility prefix if needed.
    """
    import typing as _t

    attrs: list[str] = []
    meths: list[str] = []

    # ── own annotations only ────────────────────────────────────────
    own_ann: dict[str, Any] = {}
    try:
        # Resolve own annotations against the full MRO for forward refs,
        # but only keep keys that are declared directly on this class.
        own_keys = (
            set(cls.__annotations__) if hasattr(cls, "__annotations__") else set()
        )
        if own_keys:
            try:
                all_hints = _t.get_type_hints(cls)
            except Exception:
                all_hints = getattr(cls, "__annotations__", {})
            own_ann = {k: v for k, v in all_hints.items() if k in own_keys}
    except Exception:
        own_ann = getattr(cls, "__annotations__", {})

    for an, at in own_ann.items():
        if not _pub(an):
            continue
        ts = at.__name__ if isinstance(at, type) else str(at).replace("typing.", "")
        ts = re.sub(r"[\w]+\.(?=[A-Z])", "", ts)
        attrs.append(f"{an}: {ts}")

    # ── own methods / properties / class vars ───────────────────────
    seen = {a.split(":")[0].strip() for a in attrs}
    for nm in sorted(vars(cls)):
        if not _pub(nm):
            continue
        v = vars(cls)[nm]
        if isinstance(v, (staticmethod, classmethod)):
            fn = v.__func__ if hasattr(v, "__func__") else v
            pfx = "«static» " if isinstance(v, staticmethod) else "«class» "
            meths.append(f"{pfx}{nm}{_sig(fn)}")
        elif callable(v) and not isinstance(v, type):
            meths.append(f"{nm}{_sig(v)}")
        elif isinstance(v, property):
            r = ""
            if v.fget and v.fget.__annotations__.get("return"):
                rv = v.fget.__annotations__["return"]
                r = f": {rv.__name__ if isinstance(rv, type) else str(rv)}"
            attrs.append(f"«property» {nm}{r}")
        elif nm not in seen:
            attrs.append(nm)
    return attrs, meths


def _sig(fn: Any) -> str:
    try:
        s = inspect.signature(fn)
        ps = []
        for p in s.parameters.values():
            if p.name in ("self", "cls"):
                continue
            if p.annotation is not inspect.Parameter.empty:
                t = (
                    p.annotation.__name__
                    if isinstance(p.annotation, type)
                    else str(p.annotation).replace("typing.", "")
                )
                t = re.sub(r"[\w]+\.(?=[A-Z])", "", t)
                ps.append(f"{p.name}: {t}")
            else:
                ps.append(p.name)
        r = ""
        if s.return_annotation is not inspect.Signature.empty:
            rv = s.return_annotation
            rs = rv.__name__ if isinstance(rv, type) else str(rv).replace("typing.", "")
            rs = re.sub(r"[\w]+\.(?=[A-Z])", "", rs)
            r = f" → {rs}"
        return f"({', '.join(ps)}){r}"
    except (ValueError, TypeError):
        return "()"


def _assocs(cls: Type) -> list[tuple[Type, str, str]]:
    import types as _ts
    import typing

    out: list[tuple[Type, str, str]] = []
    try:
        res = typing.get_type_hints(cls)
    except Exception:
        return out
    for an, at in res.items():
        origin = getattr(at, "__origin__", None)
        args = getattr(at, "__args__", ()) or ()
        if origin in (list, set, frozenset):
            for a in args:
                if isinstance(a, type) and a.__module__ != "builtins":
                    out.append((a, an, "*"))
        elif origin in (dict,):
            for a in args:
                if isinstance(a, type) and a.__module__ != "builtins":
                    out.append((a, an, "*"))
        elif origin is typing.Union or (
            hasattr(_ts, "UnionType") and isinstance(at, _ts.UnionType)
        ):
            for a in args:
                if (
                    isinstance(a, type)
                    and a is not type(None)
                    and a.__module__ != "builtins"
                ):
                    out.append((a, an, "0..1"))
        elif isinstance(at, type) and at is not cls and at.__module__ != "builtins":
            out.append((at, an, "1"))
    return out


def _nid(cls: Type) -> str:
    return (
        "n"
        + hashlib.md5(f"{cls.__module__}.{cls.__qualname__}".encode()).hexdigest()[:12]
    )


def _inspect_dot(cls: Type, conf: Config) -> str:
    dpi, fn, fs = (
        conf.uml_dpi,
        conf.uml_font_name,
        conf.uml_font_size,
    )
    priv, md, rd = (
        conf.uml_show_private,
        conf.uml_max_inheritance_depth,
        conf.uml_rankdir,
    )

    def _node(k: Type, main: bool) -> str:
        # a, m = _members(k, priv) if main else ([], [])
        a, m = _members(k) if main else ([], [])
        nm = k.__name__
        hbg = _P["header_bg"] if main else _P["assoc_header_bg"]
        sbg = _P["section_bg"] if main else _P["assoc_section_bg"]
        bc = _P["border"] if main else _P["assoc_border"]
        pw = "2" if main else "1"

        def _r(items: list[str]) -> str:
            if not items:
                return "<TR><TD> </TD></TR>"
            return "".join(
                f'<TR><TD ALIGN="LEFT" BALIGN="LEFT">{_esc(x)}</TD></TR>' for x in items
            )

        lb = (
            f'<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" '
            f'CELLPADDING="4" COLOR="{bc}">'
            f'<TR><TD BGCOLOR="{hbg}"><FONT COLOR="{_P["header_fg"]}"><B>'
            f"{_esc(nm)}</B></FONT></TD></TR>"
            f'<TR><TD><TABLE BORDER="0" CELLSPACING="0" CELLPADDING="2"'
            f' BGCOLOR="{sbg}">{_r(a)}</TABLE></TD></TR>'
            f'<TR><TD><TABLE BORDER="0" CELLSPACING="0" CELLPADDING="2"'
            f' BGCOLOR="{sbg}">{_r(m)}</TABLE></TD></TR>'
            f"</TABLE>>"
        )
        return f"    {_nid(k)} [label={lb}, shape=plaintext, penwidth={pw}];\n"

    vis: set[Type] = set()
    edges: list[str] = []
    nodes: list[str] = []

    def _walk(k: Type, d: int) -> None:
        if k in vis or d > md:
            return
        vis.add(k)
        nodes.append(_node(k, k is cls))
        for b in k.__bases__:
            if b is object:
                continue
            edges.append(
                f"    {_nid(b)} -> {_nid(k)} "
                f'[arrowhead=empty, color="{_P["edge_inherit"]}"];\n'
            )
            _walk(b, d + 1)

    _walk(cls, 0)

    for tgt, an, card in _assocs(cls):
        if tgt not in vis:
            nodes.append(_node(tgt, False))
            vis.add(tgt)
        lbl = f"{an} [{card}]" if card != "1" else an
        edges.append(
            f"    {_nid(cls)} -> {_nid(tgt)} "
            f'[arrowhead=open, color="{_P["edge_assoc"]}", '
            f'label="{lbl}", fontsize={fs - 1}];\n'
        )

    return (
        f"digraph UML {{\n"
        f"    graph [dpi={dpi}, rankdir={rd}, bgcolor=transparent, "
        f'fontname="{fn}", pad=0, margin=0.1];\n'
        f'    node  [fontname="{fn}", fontsize={fs}];\n'
        f'    edge  [fontname="{fn}", fontsize={fs - 1}];\n\n'
        f"{''.join(nodes)}\n{''.join(edges)}}}\n"
    )


# =====================================================================
#  Helpers
# =====================================================================


def _try_import(fqn: str) -> Optional[Type]:
    parts = fqn.split(".")
    for i in range(len(parts) - 1, 0, -1):
        try:
            mod = importlib.import_module(".".join(parts[:i]))
        except Exception:
            continue
        obj: Any = mod
        try:
            for a in parts[i:]:
                obj = getattr(obj, a)
        except AttributeError:
            continue
        if isinstance(obj, type):
            return obj
    return None


def _latex_width(width_px: float, height_px: float, dpi: int, landscape: bool) -> str:
    """
    Compute ``:width:`` so the diagram fits the page in both
    dimensions.  Returns a string like ``"10.8cm"`` or ``"100%"``.
    """
    if dpi <= 0:
        dpi = 300

    inch_to_cm = 2.54  # 1 inch = 2.54 cm

    width_cm = (width_px / dpi) * inch_to_cm
    height_cm = (height_px / dpi) * inch_to_cm

    # Scale factors to fit each dimension (1.0 = already fits)
    if landscape:
        w_scale = min(1.0, _MAX_TEXT_HEIGHT_CM / width_cm) if width_cm > 0 else 1.0
        h_scale = min(1.0, _MAX_TEXT_WIDTH_CM / height_cm) if height_cm > 0 else 1.0
    else:
        w_scale = min(1.0, _MAX_TEXT_WIDTH_CM / width_cm) if width_cm > 0 else 1.0
        h_scale = min(1.0, _MAX_TEXT_HEIGHT_CM / height_cm) if height_cm > 0 else 1.0

    # Use the MORE constraining factor
    scale = min(w_scale, h_scale)

    final_width_cm = width_cm * scale
    if (
        final_width_cm
        >= (_MAX_TEXT_HEIGHT_CM if landscape else _MAX_TEXT_WIDTH_CM) - 0.1
    ):
        return "100%"
    return f"{final_width_cm:.1f}cm"


def _fix_pdf(path: Path):
    tmp = path.with_suffix(".v15.pdf")
    out = path.with_suffix(".pdf")

    # 1) down-convert to PDF 1.5 (optional, helps version warnings)
    subprocess.run(
        [
            "gs",
            "-sDEVICE=pdfwrite",
            "-dPDFSETTINGS=/screen",
            "-dCompatibilityLevel=1.5",
            "-dDownsampleColorImages=true",
            "-dColorImageDownsampleType=/Bicubic",
            "-dColorImageResolution=72",
            "-dGrayImageDownsampleType=/Bicubic",
            "-dGrayImageResolution=72",
            "-dMonoImageDownsampleType=/Bicubic",
            "-dMonoImageResolution=72",
            "-sPAPERSIZE=a4",
            "-dFIXEDMEDIA",
            "-dPDFFitPage",
            "-dQUIET",
            "-dNOPAUSE",
            "-dBATCH",
            "-dSAFER",
            f"-sOutputFile={tmp}",
            str(path),
        ],
        check=True,
    )

    # # 2) crop to content (fixes huge MediaBox => fixes Dimension too large)
    try:
        subprocess.run(["pdfcrop", "--verbose", str(tmp), str(out)], check=True)
    except Exception as e:
        logger.info("-" * 100)
        logger.info(e)
        logger.info("-" * 100)

    # Replace original (or instead update references to use .fixed.pdf)
    out.replace(path)
    tmp.unlink(missing_ok=True)


def _fit_scale(w_cm: float, h_cm: float, max_w: float, max_h: float) -> float:
    """Return the uniform scale factor to fit (w_cm × h_cm) into (max_w × max_h)."""
    if w_cm <= 0 or h_cm <= 0:
        return 1.0
    return min(
        min(1.0, max_w / w_cm),
        min(1.0, max_h / h_cm),
    )


def _should_landscape(w_px: float, h_px: float, dpi: int) -> bool:
    """
    Decide whether landscape orientation actually helps.

    Two conditions must BOTH be met:
    1. The diagram is genuinely wide (aspect ratio ≥ 2.5:1).
       Nearly-square or moderately wide diagrams stay portrait.
    2. Landscape yields at least 20% more image area than portrait,
       confirming the rotation actually improves readability.
    """
    if h_px <= 0 or w_px <= h_px * _LANDSCAPE_MIN_RATIO:
        return False

    inch_to_cm = 2.54
    w_cm = (w_px / dpi) * inch_to_cm
    h_cm = (h_px / dpi) * inch_to_cm

    # Portrait:  15 cm wide × (20 − caption) cm tall
    p_scale = _fit_scale(
        w_cm,
        h_cm,
        _MAX_TEXT_WIDTH_CM,
        _MAX_TEXT_HEIGHT_CM,
    )
    # Landscape: 20 cm wide × (15 − caption) cm tall
    l_scale = _fit_scale(
        w_cm,
        h_cm,
        _MAX_TEXT_HEIGHT_CM,
        _MAX_TEXT_WIDTH_CM,
    )

    return l_scale > p_scale * (1.0 + _LANDSCAPE_GAIN)


# =====================================================================
#  Sphinx setup
# =====================================================================


def setup(app: Sphinx) -> dict[str, Any]:
    for k, v in _DEFAULTS.items():
        app.add_config_value(k, v, "env")

    # MUST run after autoapi's builder-inited (extension load order
    # guarantees this as long as sphinx_uml_autodoc is listed AFTER
    # autoapi.extension in conf.py extensions).
    app.connect("builder-inited", _on_builder_inited)

    app.add_latex_package("pdflscape")

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
