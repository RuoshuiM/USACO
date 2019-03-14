# -*- coding: utf-8 -*-
"""
ID: rmao101
LANG: PYTHON3
TASK: gift1
"""
fin = open("gift1.in")
fout = open("gift1.out", "w")

np = int(fin.readline()[:-1])

p = {fin.readline()[:-1]:0 for i in range(np)}

giver = fin.readline()
while giver:
    giver = giver[:-1]
    total, numRecipient = [int(s) for s in fin.readline().split(" ")]
    
    p[giver] -= total
    
    if not numRecipient == 0:
        iTotal = total // numRecipient
        for i in range(numRecipient):
            p[fin.readline()[:-1]] += iTotal
            total -= iTotal
    p[giver] += total
    giver = fin.readline()

for person, value in p.items():
    fout.write(person + " " + str(value) + "\n")
fout.close()