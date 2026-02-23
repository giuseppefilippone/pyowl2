# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

sys.path.insert(0, os.path.abspath("../../"))
sys.path.insert(0, os.path.abspath("_ext"))  # local Sphinx extensions

project = "PyOWL2"
copyright = "2025, Giuseppe Filippone"
author = "Giuseppe Filippone"
# The short X.Y version
version = "1.0.4"

# The full version, including alpha/beta/rc tags
release = "1.0.4"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",  # if you use Google/NumPy-style docstrings
    "autoapi.extension",
    "sphinx.ext.viewcode",  # optional: adds links to source code
    "sphinx_toolbox.tweaks.latex_toc",
    "sphinx.ext.graphviz",  # https://stackoverflow.com/a/59319659/14851404
    "sphinx_uml_autodoc",  # ← UML class diagram generation
    "sphinx_md_docs",  # ← custom extension to inject markdown into AutoAPI output
]

myst_enable_extensions = [
    "amsmath",
    "dollarmath",
    "colon_fence",
]
myst_dmath_double_inline = True

templates_path = ["_templates"]
exclude_patterns = ["_uml", "md"]
add_module_names = False
python_maximum_signature_line_length = 128

# -- Options for autodoc and autoapi --------------------------------------

# Tell AutoAPI where your package lives:
autoapi_dirs = ["../../pyowl2"]

# Optional customizations:
autoapi_options = [
    "members",
    "undoc-members",
    "show-inheritance",
    "show-module-summary",
    "special-members",
    "show-inheritance-diagram",
    "private-members",
]

autoapi_keep_files = True  # keep intermediate .rst files for tweaking
autoapi_template_dir = "_templates/autoapi"  # if you want to customize layout
autoapi_root = "api"  # directory name in your docs where API appears
autoapi_member_order = "groupwise"
suppress_warnings = [
    "misc.highlighting_failure",
    "autoapi.python_import_resolution",
    "docutils",
]

# -- Custom Sphinx extension: Markdown Injector --------------------------------
# LOCAL builds (with Ollama running):
sphinx_md_injector_generate = False  # runs LLM, writes .md, then injects
# Point to the directory code_documenter.py wrote into.
# Absolute path, or relative to the directory containing conf.py.
sphinx_md_injector_dir = "./md"
# (Optional) override if you changed autoapi_root from its default "autoapi"
sphinx_md_injector_autoapi_root = autoapi_root

# --- Custom Sphinx extension: UML Autodoc --------------------------------
# Optional: if you use numpy-style or Google-style docstrings and want to support them in autodoc as well as regular .rst files, configure Napoleon:
# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = True
napoleon_use_ivar = True
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = True
napoleon_type_aliases = None
napoleon_attr_annotations = True

autosummary_generate = True

# -- UML class diagram settings (sphinx_uml_autodoc) ----------------------
uml_dpi = 150  # PNG resolution
uml_output_dir = "_uml"  # image dir (relative to docs srcdir)
uml_font_name = "Sans"  # Graphviz font family
uml_font_size = 12  # base font size (pt)
uml_max_inheritance_depth = 3  # ancestor levels (pyreverse -a)
uml_association_depth = 1  # associated-class depth (pyreverse -s)
uml_show_private = True  # include _private members
uml_rankdir = "LR"  # TB | BT | LR | RL
uml_backend = "auto"  # "pyreverse" | "inspect" | "auto"

# -- Options for LaTeX math rendering ---------------------------------

mathjax_path = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"

# A dictionary that contains LaTeX snippets overriding those Sphinx usually puts into the generated .tex files.
latex_elements = {
    # "printindex": r"\def\twocolumn[#1]{#1}\sloppy\small\raggedright\printindex",
    "printindex": r"\sloppy\small\raggedright\printindex",
    "papersize": "a4paper",
    "fncychap": r"\usepackage[Bjarne]{fncychap}",
    "extraclassoptions": "openany",
    "preamble": r"""
        %% --- Fix "Dimension too large" for high-DPI PNGs ---
        %% pdfLaTeX assumes 72 DPI for images without DPI metadata,
        %% turning a 5000 px PNG into 70 inches — which overflows
        %% TeX's dimension register BEFORE any width= scaling applies.
        %% This tells pdfLaTeX to assume 300 DPI, so the same image
        %% is 16.9 cm — well within limits and close to true size.
        \pdfimageresolution=300

        \hypersetup{unicode=true}
        \DeclareUnicodeCharacter{2212}{\ensuremath{-}}

        % Redefine sphinxtheindex environment to use one column and smaller font
        \usepackage{etoolbox}
        \makeatletter
        \renewenvironment{sphinxtheindex}
            {\clearpage\footnotesize\begin{theindex}}
            {\end{theindex}\normalsize\clearpage}
        \makeatother

        \usepackage{fvextra}
        \DefineVerbatimEnvironment{Verbatim}{Verbatim}{breaklines,commandchars=\\\{\}}
        \usepackage[htt]{hyphenat}
        \sloppy
     """,
    "passoptionstopackages": r"\PassOptionsToPackage{hyphens}{url}",
    "sphinxsetup": r"verbatimwithframe=true, verbatimwrapslines=true, verbatimforcewraps=true, inlineliteralwraps=true",
}

latex_show_urls = "footnote"
latex_show_pagerefs = True
latex_domain_indices = True

# A dictionary mapping 'howto' and 'manual' to names of real document classes that will be used as the base for the two Sphinx classes.
latex_docclass = {"howto": "book", "manual": "report"}
latex_documents = [
    (
        "index",  # startdocname
        "pyowl2-documentation.tex",  # targetname  ← avoids "pyowl2.tex/pdf"
        "PyOWL 2 Documentation",  # title
        "Giuseppe Filippone",  # author
        "manual",  # theme
    ),
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]


def skip_special_members(app, what, name, obj, skip, options):
    if name in [
        "__dict__",
        "__module__",
        "__weakref__",
        "_abc_impl",
        "__slots__",
        "__annotations__",
        "__abstractmethods__",
    ]:
        return True  # Skip __dict__
    return None  # Keep everything else


def setup(app):
    app.connect("autoapi-skip-member", skip_special_members)
