#!/usr/bin/env python3
from sys import argv

with open(argv[1], 'r') as f:
    line = f.read()

coords = [0,0]
visited = {tuple(coords)}
for c in line:
    if c == '>':
        coords[0] += 1
    elif c == '<':
        coords[0] -= 1
    elif c == '^':
        coords[1] += 1
    elif c == 'v':
        coords[1] -= 1
    visited.add(tuple(coords))
print(len(visited))
