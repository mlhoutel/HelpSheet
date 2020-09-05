# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Help-Sheet'
copyright = '2020, LHOUTELLIER Maël'
author = 'LHOUTELLIER Maël'

# The full version, including alpha/beta/rc tags
release = '1.0.0'


# -- General configuration ---------------------------------------------------

# Display todos by setting to True
todo_include_todos = True

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['recommonmark','sphinx_rtd_theme','nbsphinx','sphinx_copybutton','sphinx.ext.todo']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

html_theme = 'sphinx_rtd_theme'

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'monokai'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = ['https://cdnjs.cloudflare.com/ajax/libs/jsxgraph/1.3.5/jsxgraph.css']
html_js_files = ['debug.js', 'https://cdnjs.cloudflare.com/ajax/libs/jsxgraph/1.3.5/jsxgraphcore.js', 'https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.0.0/p5.min.js']

html_title = "Sigma Help Sheets"
html_short_title = "Sigma"
html_logo = "_static/sigmwhite.svg"
html_favicon = "_static/sumblack.ico"
html_show_sourcelink = False
html_theme_options = {
    'logo_only': True,
    'prev_next_buttons_location': 'both'
}