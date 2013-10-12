HTML=index.html
STYLE=uit

$(HTML): slides.rst
	`which rst2html || which rst2html.py` \
	--stylesheet='' \
	--template=$(STYLE)/template.txt slides.rst >$(HTML)

clean:
	rm -f $(HTML)
