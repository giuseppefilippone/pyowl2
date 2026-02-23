"""
Python Codebase Documenter
==========================
Parses a Python project directory using `ast`, extracts all modules and source
code, then uses LangChain + ChatOllama to generate rich Markdown documentation.

Each .py file (excluding __init__.py) gets a one-sentence summary followed by
a detailed multi-sentence description.  Each package / sub-package gets a
description synthesised from the Markdown already produced for its children.

Usage:
    python code_documenter.py <source_directory> [--model <ollama_model>] [--output <output_dir>] [--base-url <ollama_url>]

Examples:
    python code_documenter.py ./my_project
    python code_documenter.py ./src --model codellama --output docs_md
"""

import ast
import logging
import sys
import textwrap
import typing
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

if typing.TYPE_CHECKING:
    from langchain_ollama import ChatOllama

# ──────────────────────────────────────────────
# Logging
# ──────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s │ %(levelname)-7s │ %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("documenter")

# ──────────────────────────────────────────────
# Data models
# ──────────────────────────────────────────────


@dataclass
class ModuleInfo:
    """A single .py file (never __init__.py)."""

    filepath: Path
    relative_path: str
    module_name: str  # dotted, e.g. "pkg.sub.helpers"
    source: str
    summary: str = ""  # one-liner filled by LLM
    description: str = ""  # multi-sentence filled by LLM
    markdown: str = ""  # final rendered markdown


@dataclass
class PackageInfo:
    """A directory (package / sub-package)."""

    name: str
    relative_path: str
    modules: list[ModuleInfo] = field(default_factory=list)
    sub_packages: list["PackageInfo"] = field(default_factory=list)
    summary: str = ""
    description: str = ""
    markdown: str = ""


# ──────────────────────────────────────────────
# AST – minimal structural hint for the LLM
# ──────────────────────────────────────────────


def _quick_stats(source: str) -> dict:
    """Return lightweight stats so the LLM knows the rough shape of the file.
    These stats are *never* rendered in any Markdown output."""
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return {"loc": len(source.splitlines())}

    n_classes = sum(
        1 for n in ast.iter_child_nodes(tree) if isinstance(n, ast.ClassDef)
    )
    n_funcs = sum(
        1
        for n in ast.iter_child_nodes(tree)
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))
    )

    return {
        "docstring": ast.get_docstring(tree),
        "n_classes": n_classes,
        "n_functions": n_funcs,
        "loc": len(source.splitlines()),
    }


# ──────────────────────────────────────────────
# Directory scanning
# ──────────────────────────────────────────────

SKIP_DIRS = {
    "__pycache__",
    ".git",
    ".venv",
    "venv",
    "node_modules",
    ".tox",
    ".mypy_cache",
    ".eggs",
}


def _is_skipped_dir(name: str) -> bool:
    lower = name.lower()
    return lower.startswith(".") or lower in SKIP_DIRS or lower.endswith(".egg-info")


def parse_module(filepath: Path, root_dir: Path) -> Optional[ModuleInfo]:
    try:
        source = filepath.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        log.warning("[md_injector] Could not read %s: %s", filepath, e)
        return None

    try:
        ast.parse(source, filename=str(filepath))
    except SyntaxError as e:
        log.warning("[md_injector] Syntax error in %s: %s", filepath, e)
        return None

    rel = filepath.relative_to(root_dir)
    parts = list(rel.with_suffix("").parts)
    module_name = ".".join(parts) if parts else rel.stem

    return ModuleInfo(
        filepath=filepath,
        relative_path=str(rel),
        module_name=module_name,
        source=source,
    )


def scan_directory(root_dir: Path) -> PackageInfo:
    root_dir = root_dir.resolve()

    def _scan(directory: Path, parent_name: str = "") -> PackageInfo:
        rel = directory.relative_to(root_dir) if directory != root_dir else Path(".")
        name = parent_name or root_dir.name
        pkg = PackageInfo(name=name, relative_path=str(rel))

        for pf in sorted(directory.glob("*.py")):
            if pf.name == "__init__.py":
                log.debug("[md_injector] Skipping %s", pf.relative_to(root_dir))
                continue
            mod = parse_module(pf, root_dir)
            if mod:
                pkg.modules.append(mod)
                log.debug("[md_injector] Indexed  %s", mod.module_name)

        for child in sorted(directory.iterdir()):
            if child.is_dir() and not _is_skipped_dir(child.name):
                sub_name = f"{name}.{child.name}" if parent_name else child.name
                sub_pkg = _scan(child, sub_name)
                if sub_pkg.modules or sub_pkg.sub_packages:
                    pkg.sub_packages.append(sub_pkg)

        return pkg

    return _scan(root_dir)


# ──────────────────────────────────────────────
# LLM prompts
# ──────────────────────────────────────────────

CODE_SYSTEM = textwrap.dedent(
    """\
    You are a senior Python developer and technical writer.
    Your job is to describe a Python source file.

    Rules you MUST follow:
    1. First line: a **single sentence** that summarises what the file does.
    2. Then a blank line.
    3. Then a **detailed, multi-sentence description** (at least 3-4 sentences)
       explaining purpose, design decisions, behaviour, and how the pieces
       fit together.
    4. Do NOT list, enumerate, or individually describe every function,
       class, method, import, or variable.  Mention a specific name ONLY
       when it is absolutely essential to understanding the code (for
       example, a central class that the entire file revolves around).
    5. Write in **plain English paragraphs only** — no bullet points, no
       numbered lists, no tables, no code blocks.
    6. You may use Markdown *italic* or **bold** for emphasis.
    7. Focus on *what* the code achieves and *why*, not a line-by-line
       walkthrough.
    8. NEVER use self-referential language about the file or the document
       itself.  Forbidden phrases include (but are not limited to):
       "This file ...", "This module ...", "This code ...", "This script ...",
       "The file ...", "The module ...", "The code ...", "The script ...",
       "This source file ...", "This Python file ...".
       Instead, directly describe what the software *does*.
       Bad:  "This file implements a REST API client."
       Good: "A REST API client that communicates with ..."
"""
)

PKG_SYSTEM = textwrap.dedent(
    """\
    You are a senior Python developer and technical writer.
    Your job is to describe a Python package (a directory of related modules).

    You will receive the **already-written Markdown documentation** of every
    file and sub-package inside this package.  Use that material — and ONLY
    that material — to write:

    1. First line: a **single sentence** that summarises what the package does.
    2. Then a blank line.
    3. Then a **detailed, multi-sentence description** (at least 3-4 sentences)
       explaining the package's purpose, how its files work together, the
       overall architecture, and any important design patterns.
    4. Do NOT list, enumerate, or individually describe every file, function,
       class, method, or variable.  Mention a specific name ONLY when it is
       absolutely essential to understanding the package.
    5. Write in **plain English paragraphs only** — no bullet points, no
       numbered lists, no tables, no code blocks.
    6. You may use Markdown *italic* or **bold** for emphasis.
    7. Focus on the big picture: *what* the package provides and *why* it is
       structured the way it is.
    8. NEVER use self-referential language about the package, directory, or
       the document itself.  Forbidden phrases include (but are not limited
       to): "This package ...", "This module ...", "This directory ...",
       "This sub-package ...", "The package ...", "The module ...",
       "This collection ...", "This library ...".
       Instead, directly describe what the software *does*.
       Bad:  "This package provides utilities for database access."
       Good: "A database access layer that abstracts ..."
"""
)


# ──────────────────────────────────────────────
# LLM helpers
# ──────────────────────────────────────────────


def _llm_call(llm: ChatOllama, system: str, user: str) -> str:
    from langchain_core.messages import HumanMessage, SystemMessage  # noqa: F811

    try:
        resp = llm.invoke(
            [
                SystemMessage(content=system),
                HumanMessage(content=user),
            ]
        )
        return resp.content.strip()
    except Exception as e:
        log.error("[md_injector] LLM error: %s", e)
        return f"*Description unavailable — LLM error: {e}*"


def _split_summary_description(raw: str) -> tuple[str, str]:
    """Split LLM output into (first paragraph, everything else)."""
    parts = raw.split("\n\n", 1)
    summary = parts[0].strip()
    description = parts[1].strip() if len(parts) > 1 else ""
    return summary, description


# ──────────────────────────────────────────────
# Describe a single .py file
# ──────────────────────────────────────────────


def describe_file(llm: ChatOllama, mod: ModuleInfo) -> None:
    stats = _quick_stats(mod.source)

    context_lines = [f"File: `{mod.relative_path}`  ({stats.get('loc', '?')} lines)"]
    if stats.get("docstring"):
        context_lines.append(f"Module docstring: {stats['docstring']}")
    if stats.get("n_classes"):
        context_lines.append(f"Contains {stats['n_classes']} class(es)")
    if stats.get("n_functions"):
        context_lines.append(f"Contains {stats['n_functions']} top-level function(s)")

    user_msg = (
        "\n".join(context_lines)
        + "\n\nFull source code:\n\n```python\n"
        + mod.source
        + "\n```\n\n"
        "Write the one-sentence summary on the first line, leave a blank "
        "line, then write the detailed multi-sentence description."
    )

    raw = _llm_call(llm, CODE_SYSTEM, user_msg)
    mod.summary, mod.description = _split_summary_description(raw)

    # Render markdown
    md = [
        "# Summary",
        "",
        mod.summary,
        "",
    ]
    if mod.description:
        md += ["## Description", "", mod.description, ""]

    mod.markdown = "\n".join(md)


# ──────────────────────────────────────────────
# Describe a package / sub-package
# ──────────────────────────────────────────────


def describe_package(llm: ChatOllama, pkg: PackageInfo, source_dir: Path) -> None:
    """Build the package description from already-generated child markdowns."""
    child_docs = []
    for mod in pkg.modules:
        child_docs.append(f"──── FILE: {mod.module_name} ────\n{mod.markdown}")
    for sub in pkg.sub_packages:
        child_docs.append(f"──── SUB-PACKAGE: {sub.name} ────\n{sub.markdown}")

    combined = "\n\n".join(child_docs)

    user_msg = (
        f"Package: `{pkg.name}`\n\n"
        "Below is the documentation already written for every file and "
        "sub-package inside this package:\n\n<text>" + combined + "</text>\n\n"
        "Write the one-sentence summary on the first line, leave a blank "
        "line, then write the detailed multi-sentence description."
    )

    raw = _llm_call(llm, PKG_SYSTEM, user_msg)
    pkg.summary, pkg.description = _split_summary_description(raw)

    # Render markdown with links to children
    md = [
        "# Summary",
        "",
        pkg.summary,
        "",
    ]
    if pkg.description:
        md += ["## Description", "", pkg.description, ""]

    if pkg.modules:
        md += ["## Modules", ""]
        for mod in pkg.modules:
            md.append(f"- [`{source_dir.stem}.{mod.module_name}`] — {mod.summary}")
        md.append("")

    if pkg.sub_packages:
        md += ["## Sub-packages", ""]
        for sub in pkg.sub_packages:
            md.append(f"- [`{source_dir.stem}.{sub.name}`] — {sub.summary}")
        md.append("")

    pkg.markdown = "\n".join(md)


# ──────────────────────────────────────────────
# Orchestrator — strict bottom-up
# ──────────────────────────────────────────────


def process_tree(
    llm: ChatOllama,
    source_dir: Path,
    pkg: PackageInfo,
    output_dir: Path,
    depth: int = 0,
) -> None:
    indent = "\t" * depth

    # 1) Describe every .py file first
    for mod in pkg.modules:
        log.debug("[md_injector]%s📄  %s", indent, mod.module_name)
        fname = source_dir.stem + "." + mod.module_name + ".md"
        filepath = output_dir / fname

        if filepath.exists():
            continue

        describe_file(llm, mod)
        filepath.write_text(mod.markdown, encoding="utf-8")
        log.debug("[md_injector] %s    → %s", indent, fname)

    # 2) Recurse into sub-packages (depth-first)
    for sub in pkg.sub_packages:
        process_tree(llm, source_dir, sub, output_dir, depth + 1)

    # 3) Describe the package using the children's markdowns
    if pkg.modules or pkg.sub_packages:
        log.debug("[md_injector]%s📦  %s", indent, pkg.name)
        idx = (
            "INDEX.md"
            if pkg.relative_path == "."
            else source_dir.stem
            + "."
            + pkg.relative_path.replace("/", ".")
            + "_INDEX.md"
        )
        filepath = output_dir / idx

        if not filepath.exists():
            describe_package(llm, pkg, source_dir)
            filepath.write_text(pkg.markdown, encoding="utf-8")
            log.debug("[md_injector] %s    → %s", indent, idx)


# ──────────────────────────────────────────────
# Helpers
# ──────────────────────────────────────────────


def _count_modules(pkg: PackageInfo) -> int:
    return len(pkg.modules) + sum(_count_modules(s) for s in pkg.sub_packages)


# ──────────────────────────────────────────────
# Entry point
# ──────────────────────────────────────────────


def _iter_modules(pkg: PackageInfo):
    """Yield all modules in a package tree."""
    yield from pkg.modules
    for sub in pkg.sub_packages:
        yield from _iter_modules(sub)


def process_library(output_dir: Path, source_dir: Path, model: str) -> None:
    from langchain_ollama import ChatOllama  # noqa: F811

    if not source_dir.is_dir():
        log.error("[md_injector] Source directory does not exist: %s", source_dir)
        sys.exit(1)

    output_dir.mkdir(exist_ok=True)

    log.debug("═" * 60)
    log.debug("[md_injector] Python Codebase Documenter")
    log.debug("═" * 60)
    log.debug("[md_injector] Source:  %s", source_dir)
    log.debug("[md_injector] Output:  %s", output_dir)
    log.debug("[md_injector] Model:   %s", model)
    log.debug("═" * 60)

    # Scan
    log.debug("[md_injector] Scanning ...")
    root_pkg = scan_directory(source_dir)
    total = _count_modules(root_pkg)
    if total == 0:
        log.warning(
            "[md_injector] No .py files found (excluding __init__.py) in %s", source_dir
        )
        sys.exit(0)
    log.debug("[md_injector] Found %d file(s) to document\n", total)

    # Init LLM
    log.debug("[md_injector] Connecting to Ollama (model=%s)...", model)
    llm = ChatOllama(
        model=model,
        temperature=0.2,
    )

    # Process bottom-up
    process_tree(llm, source_dir, root_pkg, output_dir)

    log.debug("═" * 60)
    log.debug("[md_injector] Documentation complete! Files written to: %s", output_dir)
    log.debug("═" * 60)


if __name__ == "__main__":
    output_dir = Path("./md")
    source_dir = Path("./pyowl2")
    model = "glm-4.7:cloud"
    process_library(output_dir, source_dir, model)
