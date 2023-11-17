# Configuration file for the Sphinx documentation builder.

import os
import sys

sys.path.insert(0, os.path.abspath(".."))

# -- Project information

project = "AgileRL"
copyright = "2023, AgileRL"
author = "Nick Ustaran-Anderegg"

release = "0.1"
version = "0.1.12"

# -- General configuration

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx_toolbox.collapse",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
intersphinx_disabled_domains = ["std"]

templates_path = ["_templates"]

# -- Options for HTML output

html_title = "AgileRL Documentation"
html_theme = "furo"
html_static_path = ["_static"]
html_css_files = ["css/custom.css"]
html_js_files = ["js/expand_sidebar.js"]
html_favicon = "_static/favicon.ico"
html_theme_options = {
    "sidebar_hide_name": True,
    "light_logo": "logo_teal.png",
    "dark_logo": "logo_white.png",
    "source_repository": "https://github.com/AgileRL/AgileRL/",
    "source_branch": "main",
    "source_directory": "docs/",
    "light_css_variables": {
        "color-brand-primary": "#245c5c",
        "color-brand-content": "#245c5c",
    },
    "dark_css_variables": {
        "color-brand-primary": "#48b8b8",
        "color-brand-content": "#48b8b8",
    },
}

# -- Options for EPUB output
epub_show_urls = "footnote"
