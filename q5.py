# -*- coding: utf-8 -*-
#問5 このファイルをサーバー名、ユーザーIDの昇順で5行だけ表示しろ
import csv
servers = []
for c in csv.reader(open('hoge.csv','r').readlines()):
	servers.append([c[0], int(c[1]), int(c[2]), c[3]])

for s in sorted(servers)[:5]:
	print s
