#!/usr/bin/env python3
from sys import argv

with open(argv[1], 'r') as f:
    lines = f.read().splitlines()

wins = []
for line in lines:
    line = line.split(': ')[1]
    winning_s, yours_s = line.split(' | ')
    winning = {int(n) for n in winning_s.split(' ') if len(n) > 0}
    yours = {int(n) for n in yours_s.split(' ') if len(n) > 0}
    intersect = winning.intersection(yours)
    wins.append(len(intersect))

cardcount = [1 for i in range(len(wins))]
for i, card in enumerate(wins):
    for j in range(cardcount[i]):
        for k in range(i + 1, min(i + card + 1, len(wins))):
            cardcount[k] += 1
print(sum(cardcount))
