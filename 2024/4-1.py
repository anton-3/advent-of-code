#!/usr/bin/env pypy3
from sys import argv
import math
import re
from pprint import pprint
from itertools import combinations, permutations
# CUSTOM LIBRARY FUNCTIONS
from lib import *

dirs = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,0), (0,1), (1,-1), (1,0), (1,1)]

lines = readfilelines()
width = len(lines[0])
height = len(lines)

count = 0
for row, line in enumerate(lines):
    for col, c in enumerate(line):
        if c != 'X':
            continue
        for dx, dy in dirs:
            endRow = row + dx * 3
            endCol = col + dy * 3
            if endRow < 0 or endCol < 0 or endRow >= height or endCol >= width:
                continue
            letters = ['X', lines[row+dx][col+dy], lines[row+dx*2][col+dy*2], lines[row+dx*3][col+dy*3]]
            if ''.join(letters) == 'XMAS':
                count += 1

print(count)
