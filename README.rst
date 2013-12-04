bible-libre
===========

Une Bible en français, libre.


Rendu avec biblification_2.py
---------------------------

biblification_2.py renvoie un fichier rst.

Par exemple:

     python biblification_2.py -tv -p nouveau-testament-commente  > rendu.t2t 

Usage: 

     biblification_2.py [-h] [-p PLAN] [-v] [-m] [-t]

Optional arguments:

-h, --help             show this help message and exit
-p PLAN                plan to be used
-v                     show verses references
-m                     show marks only
-t                     show references in titles
