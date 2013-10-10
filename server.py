#!/usr/bin/env python
import os
import bottle
from bottle import get, response, static_file, SimpleTemplate

def get_file_paths():
    files = []
    for dirpath, dirnames, filenames in os.walk('.'):
        if '.git' in dirnames:
            dirnames.remove('.git')

        for filename in filenames:
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
    if os.popen('which rst2html').read():
        program = 'rst2html'
    else:
        program = 'rst2html.py'
    
    return os.popen('rst2html'
                    ' --stylesheet=slider/slides.css'
                    ' --link-stylesheet'
                    ' --template=template.txt'
                    ' slides.rst')

@get('/<path:path>')
def files(path):
    return static_file(path, '.')

file_list_template = SimpleTemplate("""

<h1>Bottle!</h1>

<p><a href="slides.html">Start presentation</a></p>

<p><a href="server.py">server.py</a></p>

<h2>Files</h2>

<ul>
  % for file in files:
    <li><a href="{{file}}">{{file}}</a></li>
  % end
</ul>
""")

@get('/')
def file_list():
    return file_list_template.render(files=get_file_paths())

if __name__ == '__main__':
    bottle.debug(True)
    bottle.run(host='', reloader=True)
