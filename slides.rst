Bottle
------

Ole Martin Bjørndalen

\29. November 2013

http://bottlepy.org/


Bottle
------

* micro web-framework

* one file, no external dependencies

* runs on top of WSGI ("whisky")

* Python 2 / 3



Hello World
-----------

.. code-block:: python

    from bottle import route, run

    @route('/')
    def index():
        return 'Hello World!'

    run(host='localhost', port=8080)


Routing
-------

.. code-block:: python

    @get('/food')
    
    @post('/food')

    @route('/food', method='GET')

    @route('/food')
    def food():
        if request.method == 'GET': 
            ...

Templates
---------

.. code-block:: python

    from bottle import template

    @get('/hello/<name>')
    def hello(name='World'):
        return template('hello_template', name=name)

This renders `template.tpl` (from `bottle.TEMPLATE_PATH`).


View Decorator
--------------

.. code-block:: python

    @get('/hello/<name>')
    @view('hello_template')
    def hello(name='World'):
        return dict(name=name)


Request / Response
------------------

.. code-block:: python

    from bottle import request, response

    @get('/food')
    def food():
        cookie = request.get_cookie():
        ...
        response.content_type = 'text/html'
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

(Or `WTForms <http://wtforms.readthedocs.org/>`_)


Static Files
------------

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

    @get('/food')
    def food():
        # Dict is automatically converted to JSON.
        return {'type': 'Pizza', 'price': 'Free'}

    @post('/service')
    def service():
        data = request.json
        ...


App
---

.. code-block:: python

    app = Bottle()

    @app.get('/')
    def hello():
        return 'Hello World'

    parent_app = bottle.default_app()
    parent_app.mount("/hello", app)

For larger applications and reusability.


Standalone or not Standalone
----------------------------

.. code-block:: python

    import bottle

    if __name__ == '__main__':
        # Standalone web server
        bottle.run()
    else:
        # Running under another web server
        application = bottle.default_app()


Apache Config
-------------

::

  WSGIDaemonProcess yourapp user=www-data group=www-data processes=1 threads=5
  WSGIScriptAlias /ole/bottle /path/to/server.py


Debug og Auto Reloading
-----------------------

.. code-block:: python

    bottle.debug(True)
    bottle.run(reloader=True)

(Standalone server only.)


Useful Additions
----------------

* Beaker (caching)

* Cork (authentication)

* Jinja2 (more advanced templates)

* Sqlalchemy (object relational mapper)

* WTForms

(Of course, no longer one file.)


JSON-RPC
--------

.. code-block:: python

    import bottle_jsonrpc
    
    class Methods:
        def add(self, a, b):
            return a + b
    
    bottle_jsonrpc.register('/math', Methods())

http://github.com/olemb/bottle_jsonrpc


Flask
-----

Very similar, but based on Werkzeug og Jinja2.

.. code-block:: python

    from flask import Flask
    app = Flask(__name__)

    @app.route("/")
    def hello():
        return "Hello World!"

    if __name__ == "__main__":
        app.run()


Example
-------

`Filer <files>`_


The End
-------

::

    $ pip install bottle

http://bottlepy.org/
