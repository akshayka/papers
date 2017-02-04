SUMMARIES = $(wildcard summaries/*.md)
HTMLS  = $(subst summaries/,html/,$(patsubst %.md,%.html,$(SUMMARIES)))

default: $(HTMLS) index.html

clean:
	rm -f $(HTMLS)
	rm -f index.html

html/%.html: summaries/%.md include/header.html include/footer.html
	cat include/header.html > $@
	kramdown $< >> $@
	cat include/footer.html >> $@

index.html: $(HTMLS)
	cat include/index_header.html > $@
	python generate_index.py >> $@
	cat include/index_footer.html >> $@
