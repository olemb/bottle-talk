#!/bin/bash

which rst2html >/dev/null
if [ $? == 0 ]
    program=rst2html.py
then
    program=rst2html
fi

$program --template=template.txt slides.rst
