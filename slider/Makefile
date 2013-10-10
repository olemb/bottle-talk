# Include this file in 
#
#
# Todo: use default template.txt if one is not found.
# 
where-am-i = $(CURDIR)/$(word $(words $(MAKEFILE_LIST)),$(MAKEFILE_LIST))
THIS_MAKEFILE := $(call where-am-i)
HERE = $(dir $(THIS_MAKEFILE))



slides.html: slides.rst template.txt
	rst2html --stylesheet=$(HERE)/slides.css \
	--link-stylesheet --template=template.txt \
	slides.rst >slides.html

view: slides.html
	chromium-browser >/dev/null 2>/dev/null --new-window slides.html

clean:
	rm -f slides.html
