# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Fracta Language'
copyright = '2025, Fracta Language Foundation'
author = 'Fracta Language Foundation'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
html_permalinks_icon = "<span>#</span>"
html_logo = "_static/logo.png"

#master_doc = 'pages/index'

import sys, os
sys.path.insert(0, os.path.abspath('.'))

import importlib
import fractalexer

fractalexer = importlib.reload(fractalexer)

from fractalexer import FractaLexer

from sphinx.highlighting import lexers

lexers['fracta'] = FractaLexer()