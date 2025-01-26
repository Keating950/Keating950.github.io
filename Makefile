.PHONY: all pages css

all: pages css

pages:
	./gen_pages.py

css:
	sass scss:css --no-source-map --style compressed

watch:
	while true; do \
		inotifywait -e modify template.j2 css/; \
		make; \
	done
