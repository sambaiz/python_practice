# -*- coding: utf-8 -*-
#問7 このログのUU(ユニークユーザー)数を表示しろ
import csv
print(len(set(r[2] for r in csv.reader(open('hoge.csv','r')))))