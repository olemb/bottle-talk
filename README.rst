reStructuredText Slide Show
===========================

Very minimal system for HTML slide shows from `reStructuredText
<http://en.wikipedia.org/wiki/ReStructuredText>`_.


Requirements
------------

Requires ``rst2html`` (for generating the html file).

Works in Chrome / Chromiun, Firefox, Safari and Explorer 9. No support
for Explorer 8 or lower.


Creating a slide show
---------------------

Just clone this repository and modify ``slides.rst``. Run ``make`` to
build ``slides.html``.

Alternatively you can use the included web app which generates the
``slides.html`` file dynamically::

    $ ./server.py

Make targets::

    make        # creates slides.html from slides.rst
    make view   # runs "make" and opens slides.html in a web browser
                # (currently chromium-browser)
    make clean  # removes slides.html


Viewing the slideshow
---------------------

Switch the browser to fullscreen and zoom until it looks about right.

You can page through the slides with:

* page down / page up

* right arrow / left arrow

* down arrow / up arrow

* space bar / b

* left mouse button

* scroll wheel

In addition home and end can be used to go to the first and last slide
respectively.

Multitouch devices will get all slides on one page. (``slides.html``
is shown unchanged.)


How it works
------------

``rst2html`` is used to create ``slides.html`` from ``slides.rst``. A
small javascript collects all sections (div with class "section") and
puts the in a list. When key and mouse event occur, the all section
divs but the current one are hidden using css.


Modifying the templates
-----------------------

``template.txt`` contains a template for ``rst2html``. You can insert
javascript, css and other elements here. By default it is set up to
include ``slider/slider.js`` and ``slider.slider.css``, but you can
change these to style and rewrite the slide show as you like.

The default ``template.txt`` includes an extra style sheet and some
images in the template as a starting point. These reside in a
subfolder for easy reuse.


License
-------

`MIT <http://en.wikipedia.org/wiki/MIT_License>`_


Todo
----

* add some way to see all slides at once (a key?)


Contact
-------

Ole Martin Bjorndalen

ombdalen@gmail.com

ole.martin.bjorndalen@uit.no
