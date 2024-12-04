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
        if c != 'A' or row == 0 or col == 0 or row == height-1 or col == width-1:
            continue
        upleft = lines[row-1][col-1]
        upright = lines[row-1][col+1]
        downleft = lines[row+1][col-1]
        downright = lines[row+1][col+1]
        letters = [upleft,upright,downleft,downright]
        if letters.count('M') != 2 or letters.count('S') != 2 or upleft == downright or upright == downleft:
            continue
        count += 1

print(count)
