#!/usr/bin/env pypy3
from sys import argv
import math
import re
from pprint import pprint
# CUSTOM LIBRARY FUNCTIONS
from lib import *

positions = set()
lines = readfilelines()
hx = hy = tx = ty = 0
for line in lines:
    d, n = line.split()
    for i in range(int(n)):
        old_hx = hx
        old_hy = hy
        if d == 'R':
            hx += 1
        elif d == 'U':
            hy += 1
        elif d == 'L':
            hx -= 1
        else:
            hy -= 1
        dx = abs(hx-tx)
        dy = abs(hy-ty)
        if dx == 2 or dy == 2:
            tx, ty = old_hx, old_hy
        positions.add((tx, ty))
print(len(positions))
