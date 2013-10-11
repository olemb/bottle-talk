#!/usr/bin/env python
"""
Serves the presentation using Bottle.

This server is written for the Bottle talk and is not a part of rstslider.
"""
import os
import fnmatch
import bottle
from bottle import get, response, static_file, SimpleTemplate

@get('/files')
def file_list():
    return file_list_template.render(files=get_file_paths())

@get('/<path:path>')
def files(path):
    ext = os.path.splitext(path)[1]
    if ext in ['.rst', '']:
        mimetype = 'text/plain'
    else:
        mimetype = 'auto'
    return static_file(path, root='.', mimetype=mimetype)

@get('/')
def slides():
    return os.popen('`which rst2html || which rst2html.py`'
	            ' --template=template.txt slides.rst')
 
if __name__ == '__main__':
    bottle.debug(True)
    bottle.run(host='', reloader=True)
else:
    os.chdir(os.path.dirname(__file__))
    application = bottle.default_app()



#
# File listing stuff.
#

file_list_template = SimpleTemplate("""
<!doctype html>
<html>
<head><title>Bottle</title></head>
<link rel="stylesheet" href="uit/uit.css" type="text/css" />
<link rel="stylesheet" href="lib/slides.css" type="text/css" />
<body>

<div id="uit_triangle"><img src="uit/triangle.png"></div>
<div id="uit_logo"><img src="uit/logo.png"></div>

<div class="section">
<h1>Files</h1>

<p><a href="./">Back to presentation</a></p>

<ul>
  % for file in files:
    <li>
       <a href="{{file}}">{{file}}</a>
    </li>
  % end
</ul>
</div>

</body>
</html>
""")

def ignore_file(filename):
    # Can't use .gitignore here because it ignores slides.html
    # and not .git and .gitignore.
    for pattern in ['*.pyc', '*~', '.gitignore']:
        if fnmatch.fnmatch(pattern, filename):
            return True

    return False

def get_file_paths():
    files = []
    for dirpath, dirnames, filenames in os.walk('.'):
        if '.git' in dirnames:
            dirnames.remove('.git')

        for filename in filenames:
            if ignore_file(filename):
                continue

            if filename.endswith('.pyc'):
                continue

            if filename.endswith('~'):
                continue

            path = os.path.join(dirpath, filename)
            if path.startswith('./'):
                path = path[2:]

            files.append(path)

    files.sort()

    return files
