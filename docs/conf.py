# -*- coding: utf-8 -*-
#
# vtsttools documentation build configuration file
import sys, os
from datetime import date
import urllib.request
import json

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))
sys.path.append(os.path.abspath('.'))
# We need to know which version of vtstcode is the latest, this is a hack because Sphinx substitution wasn't working
github_api = "https://api.github.com/repos/henkelmangroup/vtstcode/releases/latest"
with urllib.request.urlopen(github_api) as r:
    assets = json.loads(r.read()).get("assets", [])
    #Find the vtstcode tarball asset
    vtstcode_asset = next((a for a in assets if a["name"].startswith("vtstcode") and a["name"].endswith(".tar.gz")), None)

if vtstcode_asset:
    LATEST_VTSTCODE_REV = vtstcode_asset["name"] # "vtstcode-213.tar.gz", I just want number
    LATEST_VTSTCODE_URL = vtstcode_asset["browser_download_url"]
else:
    LATEST_VTSTCODE_REV = "vtstcode-latest.tar.gz"
    LATEST_VTSTCODE_URL = "https://github.com/henkelmangroup/vtstcode/releases/latest"

def replace_rev(app,docname,source):
    source[0] = source[0].replace('$(LATEST_VTSTCODE_REV)', LATEST_VTSTCODE_REV)
    source[0] = source[0].replace('$(LATEST_VTSTCODE_URL)', LATEST_VTSTCODE_URL)

#on build, update variables
def setup(app):
    app.connect('source-read', replace_rev)
###############################################################
####                PROJECT INFO
###############################################################
project = u'vtsttools'
copyright = f'2015-{date.today().year}, Henkelman Group'
version = '3.1' #verify this
releas = '3.1'
###############################################################
####                BUILD SUPPORT
###############################################################
source_suffix = {".txt" : 'restructuredtext'}
master_doc = "index" # changed from contents to index
exclude_trees = ["_build"]
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.todo', 'sphinx.ext.coverage', 'sphinx.ext.mathjax']
htmlhelp_basename = 'vtsttoolsdoc'
templates_path = ['_templates']

pygments_style = 'sphinx'
html_static_path = ['_static']
html_theme_path = ["."]
html_theme = 'henk_theme'
html_title = "Transition State Tools for VASP"
html_short_title = "VTSTTools"
html_logo = "./_static/logo.png"
# html_css_files = ["henk_final.css"] # location relative to _static folder
# html_show_copyright = True
# html_show_sphinx = True  
html_show_search_summary = True
html_show_sourcelink = True
html_sidebars = { # NOTE: order determines order will appear in sidebar
    "**" : [
        "localtoc.html",
        "sourcelink.html"
    ]
}
html_css_files = ["henkv2.css"]
###############################################################
####                MANUAL SUPPORT
###############################################################
man_pages = [
    ('index', 'vtsttools', u'vtsttools Documentation',
     [u'Henkelman Group'], 1)
]
###############################################################
####                LATEX SUPPORT
###############################################################
# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_elements = {
}
latex_documents = [
  ('index', 'vtsttools.tex', u'vtsttools Documentation',
   u'Henkelman Group', 'manual'),
]
# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'vtsttools', u'vtsttools Documentation',
   u'Henkelman Group', 'vtsttools', 'One line description of project.',
   'Miscellaneous'),
]