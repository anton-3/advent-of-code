#!/usr/bin/env pypy3
from sys import argv
import math
import re
from pprint import pprint
# CUSTOM LIBRARY FUNCTIONS
from lib import *
from itertools import combinations

lines = readfilelines()
def distance(u, c1, c2):
    x_dist = abs(c1[0]-c2[0])
    y_dist = abs(c1[1]-c2[1])
#    l, r = sorted([c1[0], c2[0]])
    for i in range(c1[0], c2[0]):
        if u[i][0] == 'G':
            x_dist += 999999
#    l, r = sorted([c1[1], c2[1]])
    for i in range(c1[1], c2[1]):
        if u[0][i] == 'G':
            y_dist += 999999
    return x_dist + y_dist

def expand(universe):
    add_cols = []
    new = []
    for i, row in enumerate(universe):
        if set(row) == {'.'}:
            new.append(['G' for i in range(len(row))])
        else:
            new.append(list(row))
        col = [j[i] for j in universe]
        if set(col) == {'.'}:
            add_cols.append(i)
    for i in add_cols:
        for row in new:
            row[i] = 'G'
    return new

#print('\n'.join(lines))
#print('='*80)
universe = expand(lines)
#print('\n'.join([''.join(row) for row in universe]))

galaxies = set()
for i, row in enumerate(universe):
    for j, c in enumerate(row):
        if c == '#':
            galaxies.add((i, j))

lengths = 0
for pair in combinations(galaxies, 2):
    lengths += distance(universe, pair[0], pair[1])
print(lengths)
