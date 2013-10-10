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

# Figure out which program to use. This is messy.
RST2HTML_PATH = `which rst2html`
ifneq ($(RST2HTML_PATH), '')
# Use debian package installed version.
RST2HTML = rst2html
else
# Fall back on the pip installed version.
RST2HTML = rst2html.py
endif

slides.html: slides.rst template.txt
	$(RST2HTML) --template=template.txt slides.rst >slides.html

view: slides.html
	chromium-browser >/dev/null 2>/dev/null --new-window slides.html

clean:
	rm -f slides.html
