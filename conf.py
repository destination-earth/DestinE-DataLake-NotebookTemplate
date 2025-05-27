# -- Path setup -------------------------------------------------------------
import os
import sys
sys.path.insert(0, os.path.abspath('_extensions'))

# -- Project information ----------------------------------------------------
project = "Mein Cookbook"
author = "Dein Name / Team"
copyright = "2024, Dein Name"

# -- General configuration --------------------------------------------------
extensions = [
    "myst_parser",  
    "sphinx_design",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

# -- MyST Parser config -----------------------------------------------------
myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "html_image",
]

# -- Notebook config --------------------------------------------------------
nb_execution_mode = "off"

# -- HTML output ------------------------------------------------------------
html_theme = "pydata_sphinx_theme"
html_title = project
html_static_path = ['_static'] if os.path.isdir('_static') else []

# -- Root document ----------------------------------------------------------
root_doc = "index"
