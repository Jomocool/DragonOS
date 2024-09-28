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
import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'DragonOS'
copyright = '2022-2024, DragonOS Community'
author = 'longjin'
github_org = 'DragonOS-Community'
github_repo = 'DragonOS'

# The full version, including alpha/beta/rc tags
release = 'dev'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['myst_parser', 'sphinx_multiversion']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'zh_CN'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
source_suffix = ['.rst', '.md']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

html_context = dict()

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_sidebars = {
    '**': [
        'versioning.html',
    ],
}

myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

# sphinx-multiversion 指定哪个分支为 lastest 版本
smv_latest_version = 'master'
smv_released_pattern = r'^tags/.*$'           # Tags only
smv_tag_whitelist = r'^(V.*|v.*)$'
smv_branch_whitelist = "master"

# Define the canonical URL if you are using a custom domain on Read the Docs
html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "")

# Tell Jinja2 templates the build is running on Read the Docs
if os.environ.get("READTHEDOCS", "") == "True":
    html_context["READTHEDOCS"] = True

if os.environ.get("SPHINX_MULTIVERSION_GIT_COMMIT", "") != "":
    html_context["commit"] = os.environ["SPHINX_MULTIVERSION_GIT_COMMIT"]
elif os.environ.get("CURRENT_GIT_COMMIT_HASH", "") != "":
    html_context["commit"] = os.environ["CURRENT_GIT_COMMIT_HASH"]


# 截取前 7 位 commit hash，如果长度不足则不截取
if "commit" in html_context:
    html_context["commit"] = html_context["commit"][:7]
    if os.environ.get("CURRENT_GIT_COMMIT_DIRTY", "") == "1":
        html_context["commit"] += "-dirty"


# -- Set GitHub URL for Edit on GitHub links ---
html_context['display_github'] = True
html_context['github_user'] = github_org
html_context['github_repo'] = github_repo
html_context['github_version'] = html_context['commit'] if 'commit' in html_context else 'master'
html_context['conf_py_path'] = '/docs/'
