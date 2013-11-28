HTML=index.html
STYLE=uit

$(HTML): slides.rst
	`which rst2html || which rst2html.py` \
	--stylesheet='' \
	--template=$(STYLE)/template.txt slides.rst >$(HTML)
	echo `grep section index.html | wc -l` slides

clean:
	rm -f $(HTML)
