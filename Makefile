SRC  = $(wildcard *.ipynb)
MDS  = $(SRC:.ipynb=.md)
PDFS = $(SRC:.ipynb=.pdf)

all:	$(PDFS)

pdf:	clean $(PDFS)
html:	clean $(HTML)

%.md: %.ipynb
	python exporter.py $<

%.pdf: %.md
	pandoc -t beamer --slide-level 2 --template=default.beamer -o $@ $< --metadata="theme:metropolis"

clean:
	rm -f *.html *.pdf 0*.md

slides.pdf: $(MDS)
	cat 00-README.md \
		01-Indexing.md \
		02-Alignment.md \
		03-Iterators-Groupby.md \
		04-Visualization.md \
		05-Tidy-Data.md \
		06-Performance.md \
		07-Timeseries.md \
		08-Pandas-NumPy-ScikitLearn.md \
		| pandoc -t beamer --slide-level 2 \
			--template=default.beamer -o $@ --metadata="theme:metropolis"


