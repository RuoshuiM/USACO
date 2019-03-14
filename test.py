# -*- coding: utf-8 -*-
"""
ID: rmao101
LANG: PYTHON3
TASK: test
"""
fin = open("test.in")
fout = open("test.out", "w")
x,y = map(int, fin.readline().split())
sum = x+y
fout.write(str(sum) + '\n')
fout.close()