#!/usr/bin/env pypy3
from sys import argv
import math
import re
from pprint import pprint
# CUSTOM LIBRARY FUNCTIONS
from lib import *

positions = set()
lines = readfilelines()
x = [0] * 10
y = [0] * 10
for line in lines:
    d, n = line.split()
    for j in range(int(n)):
        oldx = x.copy()
        oldy = y.copy()
        if d == 'R':
            x[0] += 1
        elif d == 'U':
            y[0] += 1
        elif d == 'L':
            x[0] -= 1
        else:
            y[0] -= 1
        for i in range(9):
            dx = abs(x[i]-x[i+1])
            dy = abs(y[i]-y[i+1])
            if dx == 2 or dy == 2:
                if dx + dy == 2:
                    if x[i] > x[i+1]:
                        x[i+1] += 1
                    elif x[i] < x[i+1]:
                        x[i+1] -= 1
                    elif y[i] > y[i+1]:
                        y[i+1] += 1
                    else:
                        y[i+1] -= 1
                else:
                    # diagonal
                    if x[i] > x[i+1]:
                        nx = 1
                    else:
                        nx = -1
                    if y[i] > y[i+1]:
                        ny = 1
                    else:
                        ny = -1
                    x[i+1] += nx
                    y[i+1] += ny
        positions.add((x[-1], y[-1]))
#        print([(x[i], y[i]) for i in range(10)])
print(len(positions))
