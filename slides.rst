Bottle
------

Ole Martin Bjørndalen

\30. november 2013


Bottle
------

* mikrorammeverk for små webapplikasjoner / tjenester

* en fil, ingen eksterne avhengigheter (lett å bundle)

* kjører på WSGI

http://bottlepy.org/


Hello
-----

.. code-block:: python

    from bottle import route, run

    @route('/')
    def index():
        return 'Hello Bottle!'

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

    from bottle import get, post, request
    
    @get('/login')
    def login():
        return 'login_form_here'

    @post('/login')
    def do_login():
        username = request.forms.get('username')
        password = request.forms.get('password')
        ...

Det finnes mer avansert form-håndtering.


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

    http://some.server/get_data?id=22&page=2

.. code-block:: python

    @get('/get/data')
    def get_data():
        forum_id = request.query.id
        page = request.query.page or '1'


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

* dictionary => JSON

* '', False, None => Content-Length: 0

* unicode string => UTF-8 (or Content-Type)

* byte string => binary data

* file object => result of .read()

* iterable, generator => returns result

* HTTPError, HTTPResponse


På Apache (med WSGI)
--------------------

.. code-block:: python

    import bottle

    if __name__ == '__main__':
        # Standalone web server
        bottle.run(reloader=True)
    else:
        # Running under WSGI (probably Apache)
        application = bottle.default_app()


Lokale rutinger
---------------

Lurt for litt større applikasjoner og for gjenbrukbarhet.

.. code-block:: python

    app = Bottle()

    @app.get('/')
    def hello():
        return 'Hello World'


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

.. code-block:: bash

    from flask import Flask
    app = Flask(__name__)

    @app.route("/")
    def hello():
        return "Hello World!"

    if __name__ == "__main__":
        app.run()


Slutt
-----

.. code-block:: bash

    $ sudo pip install bottle

    $ sudo apt-get install bottle

    $ wget http://raw.github.com/defnull/bottle/master/bottle.py

http://bottlepy.org/

http://github.com/defnull/bottle/
