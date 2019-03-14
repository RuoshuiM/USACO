# -*- coding: utf-8 -*-
"""
ID: rmao101
LANG: PYTHON3
TASK: ride
"""

from string import ascii_uppercase as upcase

fin = open("ride.in")
fout = open("ride.out", "w")



ltMap = {c: i for i, c in enumerate(upcase, 1)}

p1, p2 = 1, 1

for c in fin.readline():
    p1 *= ltMap.get(c, 1)
for c in fin.readline():
    p2 *= ltMap.get(c, 1)

if p1 % 47 == p2 % 47:
    result = "GO"
else:
    result = "STAY"

fout.write(result + '\n')
fout.close()