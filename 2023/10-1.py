#!/usr/bin/env pypy3
from sys import argv
import math
import re
from pprint import pprint
# CUSTOM LIBRARY FUNCTIONS
from lib import *

lines = readfilelines()

start = None
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c == 'S':
            start = (i, j)
            break
    if start: break
print(start)

def move(coords, direction):
    match direction:
        case 'U':
            return (coords[0]-1, coords[1])
        case 'D':
            return (coords[0]+1, coords[1])
        case 'L':
            return (coords[0], coords[1]-1)
        case 'R':
            return (coords[0], coords[1]+1)

direction = 'L'
n = move(start, direction)
steps = 1
while lines[n[0]][n[1]] != 'S':
    current = lines[n[0]][n[1]]
    match current:
        case 'L':
            direction = 'U' if direction == 'L' else 'R'
        case 'J':
            direction = 'U' if direction == 'R' else 'L'
        case 'F':
            direction = 'D' if direction == 'L' else 'R'
        case '7':
            direction = 'D' if direction == 'R' else 'L'
    print(f'steps: {steps}, current: {current}, direction: {direction}')
    steps += 1
    n = move(n, direction)
print(f'steps: {steps}, current: {lines[n[0]][n[1]]}')
print(steps, steps // 2)
