Bottle
------

Ole Martin Bjørndalen

\30. november 2013

http://bottlepy.org/


Bottle
------

* mikrorammeverk for små webapplikasjoner / tjenester

* en fil, ingen eksterne avhengigheter

* kjører på WSGI ("whisky")

* Python 2 / 3



Hello World
-----------

.. code-block:: python

    from bottle import route, run

    @route('/')
    def index():
        return 'Hello World!'

    run(host='localhost', port=8080)


Litt mer avansert
-----------------

.. code-block:: python

    from bottle import template

    @route('/')
    @route('/hello/<name>')
    def index(name='Stranger'):
        return template('Hello {{name}}!', name=name)

Du kan bruke andre template-bibloteker. (Jinja2!)


GET / POST
----------

.. code-block:: python

    from bottle import get, post
    
    @get('/login')
    def login():
        ...

    @post('/login')
    def do_login():
        ...


Request / response
------------------

.. code-block:: python

    from bottle import request, response

    @get('/something')
    def something():
        cookie = request.get_cookie():
        ...
        response.content_type = 'text/html
        response.charset = 'latin9'


Query
-----

::

    http://moviedb/search?title=King+Kong

.. code-block:: python

    @get('/search')
    def movie_search():
        title = request.query.title
        if title == 'King Kong':
            ...


Forms
-----

.. code-block:: python

    @get('/login')
    def login():
        ...

    @post('/login')
    def login():
        username = request.forms.get('username')
        password = request.forms.get('password')
        if check_login(username, password):
            ...


Statiske filer
--------------

.. code-block:: python

    from bottle import static_file

    @route('/static/<filepath:path>')
    def server_static(filepath):
        return static_file(filepath,
               root='/path/to/your/static/files')


Error!
------

.. code-block:: python

    from bottle import error

    @error(404)
    def error404(error):
        return 'Nothing here, sorry'


JSON
----

.. code-block:: python

    import json
    import bottle

    @bottle.post('/some/service')
    def handler():
        # Dictionary:
        data = json.load(bottle.request.body)
        ...
        return {'id': req['id'],
                'result': result,
                'error': None}


Returverdier
------------

===============  ============
Returverdi       Resultat
===============  ============
dictionary       JSON
'', False, None  Content-Length: 0
unicode string   UTF-8 (or response.content_type / .charset)
byte string      binary data
file object      file.read()
iterable         
HTTPError        error
HTTPResponse     (response)
===============  ============


App
---

Lurt for litt større applikasjoner og for gjenbrukbarhet.

.. code-block:: python

    app = Bottle()

    @app.get('/')
    def hello():
        return 'Hello World'

    parent_app = bottle.default_app()
    parent_app.mount("/demo", app)


Apache eller ikke Apache
------------------------

.. code-block:: python

    import bottle

    if __name__ == '__main__':
        # Standalone web server
        bottle.run()
    else:
        # Running under another web server
        application = bottle.default_app()


Debug og auto-reloading
-----------------------

.. code-block:: python

    bottle.debug(True)
    bottle.run(reloader=True)


Plugins
-------

* Cork (autentisering)

* SQLite

* Sqlalchemy

* MongoDB

* Memcache

* ...


Cork
----

.. code-block:: python

    from cork import Cork

    auth = Cork('example_conf')

    @post('/login')
    def login():
        username = request.POST.get('user', '')
        password = request.POST.get('password', '')
        auth.login(username, password,
                   success_redirect='/',
                   fail_redirect='/login')


Annet
-----

* sessions

* cookies

* greenlets

* event callbacks (tornado)

* websockets


JSON-RPC
--------

.. code-block:: python

    import bottle_jsonrpc
    
    class Methods:
        def add(self, a, b):
            return a + b
    
    bottle_jsonrpc('/math', Methods())

http://github.com/olemb/bottle_jsonrpc


Flask
-----

Mye det samme, men basert på Werkzeug og Jinja2.

.. code-block:: python

    from flask import Flask
    app = Flask(__name__)

    @app.route("/")
    def hello():
        return "Hello World!"

    if __name__ == "__main__":
        app.run()


Eksempel
--------

`Filer <files>`_


Slutt
-----

::

    $ pip install bottle

http://bottlepy.org/
