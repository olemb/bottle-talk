#!/usr/bin/env python
"""
Serves the presentation using Bottle.

This server is written for the Bottle talk and is not a part of rstslider.
"""
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

def get_files():
    files = []
    for dirpath, dirnames, filenames in os.walk('.'):
        if '.git' in dirnames:
            dirnames.remove('.git')

        for filename in filenames:
            if ignore_file(filename):
                continue

            path = os.path.join(dirpath, filename)
            if path.startswith('./'):
                path = path[2:]

            files.append(path)

    files.sort()

    return files

@get('/')
def slides():
    return os.popen('`which rst2html || which rst2html.py`'
                    ' --stylesheet=""'
	            ' --template=uit/template.txt slides.rst')
 
@get('/files')
def files():
    template = SimpleTemplate(open('files.html'))
    return template.render(files=get_files())

@get('/<path:path>')
def files(path):
    ext = os.path.splitext(path)[1]
    if ext in ['.rst', '']:
        mimetype = 'text/plain'
    else:
        mimetype = 'auto'
    return static_file(path, root='.', mimetype=mimetype)

if __name__ == '__main__':
    bottle.debug(True)
    bottle.run(host='', reloader=True)
else:
    os.chdir(os.path.dirname(__file__))
    application = bottle.default_app()
