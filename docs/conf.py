"""Sphinx configuration for anchorregistry documentation."""

import os
import sys

# -- Path setup ---------------------------------------------------------------
# Allow autodoc to import the package.
# When building on ReadTheDocs, anchorregistry is installed via requirements.txt.
# For local builds, add the src directory of ar-python if needed.
# sys.path.insert(0, os.path.abspath("../../ar-python/src"))

# -- Project information ------------------------------------------------------
project = "anchorregistry"
author = "Ian Moore"
copyright = "2026, Ian Moore"
release = "0.1.3"

# -- General configuration ----------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",   # Google/NumPy style docstrings
    "sphinx.ext.viewcode",   # source code links
    "nbsphinx",              # Jupyter notebook rendering
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "**.ipynb_checkpoints"]

# -- HTML output --------------------------------------------------------------
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

html_theme_options = {
    "navigation_depth": 3,
    "titles_only": False,
}

# -- nbsphinx -----------------------------------------------------------------
# Notebooks are pre-executed with saved output.
# Build is fast and reliable — no RPC endpoint needed at build time.
# Set to "always" for live execution (requires RPC endpoint during build).
nbsphinx_execute = "never"

# -- autodoc ------------------------------------------------------------------
autodoc_member_order = "bysource"
autodoc_default_options = {
    "members": True,
    "show-inheritance": True,
}
