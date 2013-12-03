#!/usr/bin/python
# -*- coding: utf8 -*-

import csv
import argparse

def parseText(t):
    t = t.replace("\\n", "\n")
    t = t.replace("\\q", "\t")
    t = t.replace("\\p", "\n\n")

    return t

def getText(book, startChapter, startVerse, endChapter, endVerse, title, showVerses, showMarks):
    r = ""
    with open('textes/' + book + ".csv", 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        within = False
        for row in reader:
            if row[0] == startChapter and row[1] == startVerse:
                within = True
            if within:
                    rr = parseText(row[2]) + " "
                    if showVerses: rr = " ``{}:{}`` ".format(row[0], row[1]) + rr
                    if showMarks and not showVerses: rr = rr + " ``°`` "
                    r += rr
                    #r += "({}:{}) ".format(row[0], row[1])
            if row[0] == endChapter and row[1] == endVerse:
                break
    return r

def addTitle(row):
    return "\n\n" + "=" * int(row[1]) + row[6] + "=" * int(row[1]) + "\n"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='This generates a t2t bible.')
    parser.add_argument('-p', '--plan', help='plan to be used',
                        default="nouveau-testament-commente")
    #parser.add_argument('-s', '--style', help='style used',
                        #default="default")
    parser.add_argument('-v', help='show verses references', action='store_const', const=True, default=False)
    parser.add_argument('-m', help='show marks only', action='store_const', const=True, default=False)

    #parser.add_argument('output', help='output file')
    args = parser.parse_args()

    plan = args.plan
    #style = args.style
    #output = args.output
    showVerse = args.v
    showMarks = args.m

    text = "\n\n%!encoding: UTF-8\n"

    with open('plans/' + plan + ".csv", 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')

        r = 0
        struct = []
        for row in reader:
            if r != 0:
                struct.append(row)
            r += 1
        for i in range(len(struct)):
            row = struct[i]
            nextRow = -1
            text += addTitle(row)
            if i != len(struct) - 1: nextRow = struct[i + 1]
            if nextRow != -1 and nextRow[2] == row[2] and nextRow[3] == row[3]:
                pass
            else:
                text += getText(row[0], row[2], row[3], row[4], row[5], row[6], showVerse, showMarks)

        print text
