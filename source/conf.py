# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import datetime

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = "eduTAP"
copyright = f"{datetime.date.today().year}, eduTAP team and contributors"
author = "eduTAP team and contributors"

# The full version, including alpha/beta/rc tags
release = "v2.0.0alpha1"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_parser",
    "sphinx.ext.githubpages",
    "sphinx_copybutton",
    "sphinx_issues",
    "sphinxcontrib.mermaid",
    "sphinx.ext.todo",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinxcontrib.autodoc_pydantic",
    # The esc_router_api landing page uses grids and cards.
    "sphinx_design",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    # The package documentation is symlinked in from each submodule's own `docs/`
    # directory, so whatever else lives there arrives with it: the package's own
    # Sphinx configuration, its build output, its documentation virtualenv, and its
    # working documents. None of that belongs in this build.
    "packages/*/conf.py",
    "packages/*/_build/**",
    "packages/*/.venv/**",
    "packages/*/superpowers/**",
]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"
html_title = "eduTAP Project"

# html_logo = "_static/logo.svg"
# html_favicon = "_static/favicon.ico"
# html_logo = "_static/project-logo.png"
html_favicon = "_static/favicon.ico"
html_theme_options = {
    "icon_links": [
        {
            # Label for this link
            "name": "Website",
            # URL where the link will redirect
            "url": "https://edutap.eu/",  # required
            # Icon class (if "type": "fontawesome"), or path to local image (if "type": "local")
            "icon": "fa fa-globe",
            # The type of image to be used (see below for details)
            "type": "fontawesome",
        },
        {
            # Label for this link
            "name": "GitHub eduTAP core",
            # URL where the link will redirect
            "url": "https://github.com/edutap-eu/",  # required
            # Icon class (if "type": "fontawesome"), or path to local image (if "type": "local")
            "icon": "fa-brands fa-square-github",
            # The type of image to be used (see below for details)
            "type": "fontawesome",
        },
        {
            # Label for this link
            "name": "GitHub eduTAP community components",
            # URL where the link will redirect
            "url": "https://github.com/edutap-collective/",  # required
            # Icon class (if "type": "fontawesome"), or path to local image (if "type": "local")
            "icon": "fa-brands fa-square-github",
            # The type of image to be used (see below for details)
            "type": "fontawesome",
        },
        {
            # Label for this link
            "name": "GitHub eduTAP doccumentation issues",
            # URL where the link will redirect
            "url": "https://github.com/edutap-eu/documentation/issues",  # required
            # Icon class (if "type": "fontawesome"), or path to local image (if "type": "local")
            "icon": "fa-brands fa-square-github",
            # The type of image to be used (see below for details)
            "type": "fontawesome",
        },
    ],
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]


# -- Options for MyST -------------------------------------------------

myst_enable_extensions = [
    "deflist",
    "fieldlist",
    "colon_fence",
    # "linkify",
    "tasklist",
]

# -- Options for sphinx.ext.autodoc -----------------------------------

# -- Options for linkcheck --------------------------------------------

linkcheck_exclude_documents = [
    r"packages/.*/_autosummary/.*",
]

# -- Options for Sphinx.ext.todo --------------------------------------

todo_include_todos = True
