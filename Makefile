HTML=index.html

$(HTML): slides.rst template.txt
	`which rst2html || which rst2html.py` \
	--stylesheet='' \
	--template=template.txt slides.rst >$(HTML)

clean:
	rm -f $(HTML)
