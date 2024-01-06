#!/usr/bin/env pypy3
from sys import argv
import math
import re
from pprint import pprint
# CUSTOM LIBRARY FUNCTIONS
from lib import *
from itertools import combinations

lines = readfilelines()
def distance(c1, c2):
    return abs(c1[0]-c2[0]) + abs(c1[1]-c2[1])

def expand(universe):
    add_rows = []
    add_cols = []
    new = []
    for i, row in enumerate(universe):
        new.append(list(row))
        if set(row) == {'.'}:
            new.append(list(row))
        col = [j[i] for j in universe]
#        print(set(col))
        if set(col) == {'.'}:
            add_cols.append(i)
    for i in reversed(add_cols):
        for row in new:
            row.insert(i, '.')
    return new

universe = expand(lines)
#print('\n'.join([''.join(row) for row in universe]))

galaxies = set()
for i, row in enumerate(universe):
    for j, c in enumerate(row):
        if c == '#':
            galaxies.add((i, j))

lengths = 0
for pair in combinations(galaxies, 2):
    lengths += distance(pair[0], pair[1])
print(lengths)
