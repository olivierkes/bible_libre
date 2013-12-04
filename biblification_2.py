#!/usr/bin/python
# -*- coding: utf8 -*-

import csv
import argparse
import re


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

    text = ""

    def parseText(t):

        a = re.compile('\[(\d*)\:(\d*)\]')
        if showVerse:
            s = r':sup:`\1:\2` '
        elif showMarks:
            s = r"° "
        else:
            s = r""
        t = a.sub(s, t)

        return t

    def addMark(t):
        i = -1
        while t[i] in ["\n", "\t"]:
            i -= 1
        return t[:i] + " °" + t[i:]

    def getText(book, startChapter, startVerse, endChapter, endVerse, title, showVerses, showMarks):
        r = ""
        f = open('textes/' + book + "_2.txt", 'r')
        text = f.read()
        f.close()
        start = text.find("[{}:{}]".format(startChapter, startVerse))
        end = text.find("[{}:{}]".format(endChapter, str(int(endVerse) + 1)))
        if end < 0:
            end = text.find("[{}:{}]".format(str(int(endChapter) + 1), 1))
        return parseText(text[start:end])

    def addTitle(row):
        charSet = "#=-~_"
        return "\n\n" + row[6] + "\n" + charSet[int(row[1])] * len(row[6]) + "\n"


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
