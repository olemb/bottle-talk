HTML=index.html

$(HTML): slides.rst template.txt
	`which rst2html || which rst2html.py` \
	 --template=template.txt slides.rst >$(HTML)

view: $(HTML)
	chromium-browser >/dev/null 2>/dev/null --new-window $(HTML)

clean:
	rm -f $(HTML)
