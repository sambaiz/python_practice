# -*- coding: utf-8 -*-
#問2 このファイルからサーバー名とアクセス先だけ表示しろ
import csv
for c in csv.reader(open('hoge.csv','r')):
	print ','.join((c[0],c[3]+'\n')),
