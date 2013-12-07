

all: 	
	make rendu.rst
	make rendu.html
	make rendu.tex
	make clean
	
%.rst : 
	python biblification_2.py -t > rendu.rst
	
%.html: %.rst 
	rst2html --stylesheet=styles/default.css $*.rst > $*.html

%.tex: %.rst
	rst2xetex $*.rst > $*.tex

%.pdf: %.tex
	-xelatex $*.tex

clean:
	rm -f *.aux *.log *.out *.toc

# On efface pas les fichiers de manière générique pour le moment.
# Pour garder les autres choses du dépôt ;)
mrproper:
	make clean
	rm -f rendu.rst rendu.html rendu.pdf
