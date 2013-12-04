#!/usr/bin/python
# -*- coding: utf8 -*-

import re


def livreSuivant(text):
    titre = ""
    bookNumber = 0
    bible = []
    book = []
    chap = []
    for i in range(len(text)):
        if i == 0:
            bookTitle = text[0]
            bookNumber = bookNumber + 1
        # Si c'est la dernière ligne, on ajoute le dernier livre
        elif i == len(text) - 1:
            bible.append(book)
        else:
            # Titre de chapitre
            if re.compile('(.+)\s+(\d)+').match(text[i]):
                if chap:
                    book.append(chap)
                    chap = []

            # Nouveau livre
            elif re.compile('\d?\s?[A-ZÉÈ]{3}.*').match(text[i]):
                book.append(chap)
                chap = []
                bible.append(book)
                book = []
                bookTitle = text[i]
                bookNumber = bookNumber + 1
                chap = []
            else:
                chap.append(text[i])
    return bible

if __name__ == "__main__":
    f = open('1-66.txt', 'r')
    fichier = f.read()
    f.close()

    fichier = fichier.split("\n")

    # Nettoyage
    text = []
    for l in fichier:
        l = l.strip()
        if l != "":
            text.append(l)

    # Séparation en livres
    livres = []
    bible = livreSuivant(text)
    print(len(bible), len(bible[0])) # pour vérification

    # Génère les CSV
    for b in bible:
        bookNumber = bible.index(b) + 1
        f = open('{}.csv'.format(bookNumber), 'w')
        for c in b:
            for v in c:
                chapNumber = b.index(c) + 1
                verseNumber = c.index(v) + 1
                m = re.compile(r"\d+.?\s(.*)").match(v)
                if m:
                    verse = m.group(1)
                else:
                    print(v)
                f.write('{},{},"{}"\n'.format(chapNumber, verseNumber, verse))
        f.close()

    # Génère les TXT
    for b in bible:
        bookNumber = bible.index(b) + 1
        f = open('{}.txt'.format(bookNumber), 'w')
        for c in b:
            for v in c:
                chapNumber = b.index(c) + 1
                verseNumber = c.index(v) + 1
                m = re.compile(r"\d+.?\s(.*)").match(v)
                if m:
                    verse = m.group(1)
                else:
                    print(v)
                f.write('[{}:{}]{}\n'.format(chapNumber, verseNumber, verse))
        f.close()

