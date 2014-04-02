# -*- coding: utf-8 -*-
#問9 このログのserverという文字列をxxxという文字列に変え、サーバー毎のアクセス数を表示しろ
import csv,collections

hoge = collections.Counter(map(lambda x: x.replace('server', 'xxx'), [r[0] for r in csv.reader(open('hoge.csv','r'))]))
print map(lambda x, y: y + x.replace('server', 'xxx'),['server123', 'serverserver'], ['aaa', 'bbb'])
for i in hoge.most_common():
	print i