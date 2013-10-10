reStructuredText Slide Show
===========================

Very minimal system for HTML slide shows from rst.


Requirements
------------

Requires rst2html (for generating the html file).

No support for Explorer 8 or lower.


Creating a slide show
---------------------

#. create a directory and copy the ``slider`` directory there::

    $ mkdir slideshow
    $ cd slideshow
    $ cp /path/to/slider .

#. copy ``template.txt`` and modify to your needs.

#. create a Makefile::

    $ cat >>Makefile "include slider/Makefile"

#. write your presentation in ``slides.rst``

#. build the html file::

    $ make

#. view the result::

    $ make view

#. goto 4.


The rst file
------------

Each section in the rst file will be a slide, for example::

    First slide!
    ------------

    Some text.


    Second slide!
    -------------

    Some text here as well.

You can use any rst syntax that rst2html handles.


Clicking
--------

* next slide: page down, right arrow, down arrow, space bar

* previous slide: page up, left arrow, up arrow, b

* first slide: home

* last slide: end


How it works
------------

A small javascript collects all sections (div with class "section") in
a list and uses css to show and hide them as you press keys.


Contact
-------

Ole Martin Bjorndalen

ombdalen@gmail.com

ole.martin.bjorndalen@uit.no

