#!/usr/bin/python
# -*- coding: utf8 -*-

import csv
import argparse
import re


if __name__ == "__main__":
    # Parsing arguments
    parser = argparse.ArgumentParser(description='This generates a t2t bible.')
    parser.add_argument('-p', '--plan', help='plan to be used',
                        default="nouveau-testament-commente")
    parser.add_argument('-v', help='show verses references',
                        action='store_const', const=True, default=False)
    parser.add_argument('-m', help='show marks only',
                        action='store_const', const=True, default=False)
    parser.add_argument('-t', help='show references in titles',
                        action='store_const', const=True, default=False)
    args = parser.parse_args()

    plan = args.plan
    showVerse = args.v
    showMarks = args.m
    showInTitles = args.t

    text = ""

    def parseText(t):
        "Format verse references in the chosen way."
        a = re.compile('\[(\d*)\:(\d*)\]')
        if showVerse:
            s = r':sup:`\1:\2` '
        elif showMarks:
            s = r"° "
        else:
            s = r""
        t = a.sub(s, t)
        return t

    def getText(book, startChapter, startVerse, endChapter, endVerse):
        "Renvoie le texte demandé."
        r = ""
        f = open('textes/' + book + "_2.txt", 'r')
        text = f.read()
        f.close()
        start = text.find("[{}:{}]".format(startChapter, startVerse))
        end = text.find("[{}:{}]".format(endChapter, str(int(endVerse) + 1)))
        if end < 0:  # Chapitre suivant
            end = text.find("[{}:{}]".format(str(int(endChapter) + 1), 1))
        if end < 0:  # Fin du livre
            end = len(text)
        return parseText(text[start:end])

    def makeTitle(row):
        "Renvoie un titre formatté comme il faut."
        charSet = "#=-~_"
        titre = row[6]
        if showInTitles:  # ajoute la référence si demandée
            if row[2] == row[4]:
                if row[3] == row[5]:
                    tt = "{},{}".format(row[2], row[3])
                else:
                    tt = "{},{}-{}".format(row[2], row[3], row[5])
            else:
                tt = "{},{} – {},{}".format(row[2], row[3], row[4], row[5])

            # Ajoute la référence au titre, différement suivant le niveau
            if row[1] == "1":
                titre = "{}: {}".format(tt, titre)
            else:
                titre = "{} ({})".format(titre, tt)

        t = "\n\n" + titre + "\n" + charSet[int(row[1])] * len(titre) + "\n"
        return t

    with open('plans/' + plan + ".csv", 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        r = 0
        struct = []
        for row in reader:
            if r != 0:
                struct.append(row)
            r += 1
        for i in range(len(struct)):
            # Row: 0 = Livre           1 = Niveau          2 = chapitre début
            #      3 = verset debut    4 = chapitre fin    5 = verset fin
            #      6 = Titre
            row = struct[i]
            nextRow = -1
            text += makeTitle(row)
            if i != len(struct) - 1:
                nextRow = struct[i + 1]
            if nextRow != -1 and nextRow[2] == row[2] and nextRow[3] == row[3]:
                pass
            else:
                text += getText(row[0], row[2], row[3], row[4], row[5])

        print text
