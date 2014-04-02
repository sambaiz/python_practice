# -*- coding: utf-8 -*-
#問8 このログのアクセス先ごとにアクセス数を数え上位1つを表示しろ
import csv,collections
common = collections.Counter(r[1] for r in set((r[2],r[3]) for r in csv.reader(open('hoge.csv','r')))).most_common(1)
print common[0][0]