# -*- coding: utf-8 -*-
#問3 このファイルからserver4の行だけ表示しろ
import re, csv
p = re.compile('^server(\d+)')
for str in open('hoge.csv','r').readlines():
	if(p.match(str).group(1) == '4'):
		print str,
