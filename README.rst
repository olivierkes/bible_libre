bible-libre
===========

Une Bible en français, libre.


Rendu avec biblification.py
---------------------------

biblification.py renvoie un fichier txt2tags (http://txt2tags.org)

Utilisation, par exemple:

     python biblification.py -v   > rendu.t2t 

Le rendu se fait ensuite avec txt2tags, par exemple:

     txt2tags -t html --style styles/default.css rendu.t2t 
