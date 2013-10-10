include slider/Makefile

publish:
	rsync -avt --exclude='.git' --exclude='.gitignore' \
        ./ nerdly.info:web/bottle/

