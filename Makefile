

all: 	
	make rendu.rst
	make html
	make rendu.tex
	make clean
	
rendu.rst : 
	python biblification_2.py -t > rendu.rst
	


html: rendu.rst 
	rst2html --stylesheet=styles/default.css rendu.rst > rendu.html

rendu.tex: rendu.rst
	rst2xetex rendu.rst > rendu.tex

pdf: rendu.rst rendu.tex
	-xelatex rendu.tex

clean:
	rm -f rendu.aux rendu.log rendu.out rendu.toc

clean-all:
	make clean
	rm -f rendu.rst rendu.html rendu.pdf
