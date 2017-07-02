SRC  = $(wildcard notebooks/*.ipynb)
MDS  = $(patsubst notebooks/%.ipynb, markdown/%.md, $(SRC))
PDFS = $(patsubst markdown/%.md, markdown/%.pdf, $(MDS))

all:	$(PDFS)

pdf:	clean $(PDFS)
html:	clean $(HTML)

markdown/%.md: notebooks/%.ipynb
	python exporter.py $<

pdfs/%.pdf: markdown/%.md
	pandoc -t beamer --slide-level 2 --template=default.beamer -o $@ $< --metadata="theme:metropolis"

clean:
	rm -f *.html *.pdf 0*.md

slides.pdf: $(MDS)
	pandoc metadata.yaml \
		markdown/00-README.md \
		markdown/01-Indexing.md \
		markdown/02-Alignment.md \
		markdown/03-Iterators-Groupby.md \
		markdown/04-Visualization.md \
		markdown/05-Tidy-Data.md \
		markdown/06-Performance.md \
		markdown/07-Timeseries.md \
		markdown/08-Pandas-NumPy-ScikitLearn.md \
		-t beamer --slide-level 2 --latex-engine=xelatex -V theme:metropolis -o $@
