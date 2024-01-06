#!/usr/bin/env pypy3
from sys import argv
import math
import re
from pprint import pprint
# CUSTOM LIBRARY FUNCTIONS
from lib import *

lines = readfilelines()
forest = [list(map(int, list(line))) for line in lines]
visible = set()

def listcol(col):
    return [forest[i][col] for i in range(len(forest))]

for z in range(len(forest)//2):
    for i, row in enumerate(forest):
        for j, tree in enumerate(row):
            c = (i, j)
            left = max(row[:j]) if j > 0 else -1
            if left < tree:
                visible.add(c)
                continue
            right = max(row[j+1:]) if j+1 < len(forest) else -1
            if right < tree:
                visible.add(c)
                continue
            col = listcol(j)
            up = max(col[:i]) if i > 0 else -1
            if up < tree:
                visible.add(c)
                continue
            down = max(col[i+1:]) if i+1 < len(forest) else -1
            if down < tree:
                visible.add(c)
                continue

print(len(visible))
