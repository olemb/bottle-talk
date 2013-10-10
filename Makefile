slides.html: slides.rst template.txt
	slider/make_slides.sh >slides.html

view: slides.html
	chromium-browser >/dev/null 2>/dev/null --new-window slides.html

clean:
	rm -f slides.html
