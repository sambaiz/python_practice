# -*- coding: utf-8 -*-
#問6 このファイルには重複行がある。重複行はまとめて数え行数を表示しろ
print(len(set(open('hoge.csv','r'))))