# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "PyOWL2"
copyright = "2025, Giuseppe Filippone"
author = "Giuseppe Filippone"
# The short X.Y version
version = "1.0.3"

# The full version, including alpha/beta/rc tags
release = "1.0.3"

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
]

templates_path = ["_templates"]
exclude_patterns = []
add_module_names = False
python_maximum_signature_line_length = 128

# Tell AutoAPI where your package lives:
autoapi_dirs = ["../../pyowl2"]

# Optional customizations:
autoapi_options = [
    "members",
    "undoc-members",
    "show-inheritance",
    "show-module-summary",
    "special-members",
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

# Optional: if you use numpy-style or Google-style docstrings
napoleon_google_docstring = True
napoleon_numpy_docstring = True

autosummary_generate = True

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
        \hypersetup{unicode=true}

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

# A dictionary mapping 'howto' and 'manual' to names of real document classes that will be used as the base for the two Sphinx classes.
latex_docclass = {"howto": "book", "manual": "report"}


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
