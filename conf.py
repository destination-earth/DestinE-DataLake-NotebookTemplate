# -- Project information -----------------------------------------------------
project = 'My Example Cookbook'
author = 'Submitted via Cookbook System'

# -- General configuration ---------------------------------------------------
extensions = [
    "myst_parser",                # Wichtig für Markdown
    "myst_nb",                    # Für Jupyter Notebooks
    "sphinx.ext.githubpages",    # Für GitHub Pages Support
    "sphinx_design",             # Für schöne Layout-Komponenten
]

source_suffix = {
    ".md": "markdown",
    ".ipynb": "myst-nb",
}

root_doc = "index"

myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "html_image",
    "dollarmath",
]

nb_execution_mode = 'off'

exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
]  

# -- HTML output configuration -----------------------------------------------
html_theme = 'pydata_sphinx_theme'

html_theme_options = {
    "logo": {
        "text": "Cookbook",
    },
    "navigation_with_keys": True,
    "show_nav_level": 2,
    "navigation_depth": 2,
    "collapse_navigation": False,
}

html_static_path = ['_static']
