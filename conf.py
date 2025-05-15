project = 'My Example Cookbook'

extensions = [
    "myst_nb",
    "sphinx.ext.githubpages",
    "sphinx_design",
]

html_theme = 'pydata_sphinx_theme'

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

html_theme_options = {
    "logo": {
        "text": "Cookbook",
    },
    "navigation_with_keys": True,
    "show_nav_level": 2,
    "navigation_depth": 2,
    "collapse_navigation": False,
}

exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
]  

html_static_path = ['_static']
