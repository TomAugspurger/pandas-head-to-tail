SRC  = $(wildcard notebooks/*.ipynb)

strip:
	nbstripout notebooks/*.ipynb
