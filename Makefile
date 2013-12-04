

all: 	
	make rst2
	make html
	make tex
	make clean

rst : 
	python biblification.py -v > rendu.rst
	
rst2 : 
	python biblification_2.py -t > rendu.rst
	


html:
	python biblification_2.py -tv > rendu.rst
	rst2html --stylesheet=styles/default.css rendu.rst > rendu.html
	make clean
	rm rendu.rst

tex:
	python biblification_2.py -t > rendu.rst
	rst2xetex rendu.rst > rendu.tex
	rm rendu.rst

pdf:
	make tex
	-xelatex rendu.tex
	rm -f rendu.rst rendu.tex
	make clean

clean:
	rm -f rendu.aux rendu.log rendu.out rendu.toc

clean-all:
	make clean
	rm -f rendu.rst rendu.html rendu.pdf
