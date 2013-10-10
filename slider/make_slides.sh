#!/bin/bash

program=rst2html
which $program >/dev/null || program=rst2html.py
$program --template=template.txt slides.rst
