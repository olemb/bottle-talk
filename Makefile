slides.html: slides.rst template.txt
	rst2html --stylesheet=slides.css \
	--link-stylesheet --template=template.txt \
	slides.rst >slides.html

view: slides.html
	chromium-browser >/dev/null 2>/dev/null --new-window slides.html

clean:
	rm -f slides.html
