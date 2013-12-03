

all: 	
	make rst 
	make html
	make tex
	make clean

rst : 
	python biblification.py -v > rendu.rst

html:
	rst2html --stylesheet=styles/default.css rendu.rst > rendu.html

tex:
	rst2xetex rendu.rst > rendu.tex
	-xelatex rendu.tex
	
clean:
	rm rendu.aux rendu.log rendu.out rendu.toc
