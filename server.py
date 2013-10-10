#!/usr/bin/env python
import os
import fnmatch
import bottle
from bottle import get, response, static_file, SimpleTemplate

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

    return files

@get('/slides.html')
def slides():
    return os.popen('slider/make_slides.sh')

@get('/<path:path>')
def files(path):
    return static_file(path, '.')

file_list_template = SimpleTemplate("""
<!doctype html>
<html>
<head><title>Bottle</title></head>
<link rel="stylesheet" href="uit/uit.css" type="text/css" />
<link rel="stylesheet" href="slider/slides.css" type="text/css" />
<body>

<div id="uit_triangle"><img src="uit/triangle.png"></div>
<div id="uit_logo"><img src="uit/logo.png"></div>

<div class="section">
<h1>Bottle!</h1>

<p><a href="slides.html" style="font-size: 400%">Start presentation</a></p>

<p><a href="server.py">server.py</a></p>

<h2>Files</h2>

<ul>
  % for file in files:
    <li><a href="{{file}}">{{file}}</a></li>
  % end
</ul>
</div>

</body>
</html>
""")

@get('/')
def file_list():
    return file_list_template.render(files=get_file_paths())

if __name__ == '__main__':
    bottle.debug(True)
    bottle.run(host='', reloader=True)
else:
    application = bottle.default_application()

