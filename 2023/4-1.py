#!/usr/bin/env python3
from sys import argv

with open(argv[1], 'r') as f:
    lines = f.read().splitlines()

points = 0
for line in lines:
    line = line.split(': ')[1]
    winning_s, yours_s = line.split(' | ')
    winning = {int(n) for n in winning_s.split(' ') if len(n) > 0}
    yours = {int(n) for n in yours_s.split(' ') if len(n) > 0}
    intersect = winning.intersection(yours)
    card_points = 2 ** (len(intersect) - 1) if len(intersect) > 0 else 0
    points += card_points
print(points)
