# Include this file in 
#
#
# Todo: use default template.txt if one is not found.
# 

# Complicated way to get relative path to the directory of this file.
where-am-i = $(CURDIR)/$(word $(words $(MAKEFILE_LIST)),$(MAKEFILE_LIST))
THIS_MAKEFILE := $(call where-am-i)
HERE_ABS = $(dir $(THIS_MAKEFILE))
HERE = `python -c "import os.path; print(os.path.relpath('$(HERE_ABS)'))"`

slides.html: slides.rst template.txt
	rst2html --template=template.txt \
	slides.rst >slides.html

view: slides.html
	chromium-browser >/dev/null 2>/dev/null --new-window slides.html

clean:
	rm -f slides.html
