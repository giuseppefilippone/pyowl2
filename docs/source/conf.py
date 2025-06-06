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
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",  # for summary tables
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",  # if you use Google/NumPy-style docstrings
    "sphinx.ext.viewcode",  # optional: adds links to source code
]

templates_path = ["_templates"]
exclude_patterns = []

# Optional: if you use numpy-style or Google-style docstrings
napoleon_google_docstring = True
napoleon_numpy_docstring = True

autosummary_generate = True

# -- Options for LaTeX math rendering ---------------------------------

mathjax_path = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"

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
    app.connect("autodoc-skip-member", skip_special_members)
