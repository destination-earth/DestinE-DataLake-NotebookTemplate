# -- Path setup -------------------------------------------------------------
import os
import sys
sys.path.insert(0, os.path.abspath('_extensions'))

# -- Project information ----------------------------------------------------
project = "Mein Cookbook"
author = "Dein Name / Team"
copyright = "2024, Dein Name oder Organisation"

# -- General configuration --------------------------------------------------
extensions = [
    "myst_parser",      # für Markdown
    "myst_nb",          # für Jupyter Notebooks
    "sphinx_design",    # optional für schönere Layouts
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
    ".ipynb": "myst-nb",
}

# -- MyST Parser Konfiguration (Markdown) -----------------------------------
myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "html_image",
]

# -- Jupyter Notebook Konfiguration -----------------------------------------
nb_execution_mode = "off"  # Notebooks werden NICHT beim Bauen ausgeführt

# -- HTML output ------------------------------------------------------------
html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]

# -- Optional: Titelseite und Logo ------------------------------------------
html_title = project
# html_logo = "_static/logo.svg"
# html_favicon = "_static/favicon.ico"

# -- Hauptseite der Dokumentation -------------------------------------------
master_doc = "index"