#!/usr/bin/env python3
from sys import argv

with open(argv[1], 'r') as f:
    line = f.read()

coords = [0,0]
coords2 = [0,0]
visited = {tuple(coords)}
for i, c in enumerate(line):
    new = [0,0]
    if c == '>':
        new[0] += 1
    elif c == '<':
        new[0] -= 1
    elif c == '^':
        new[1] += 1
    elif c == 'v':
        new[1] -= 1
    a = coords if i % 2 == 0 else coords2
    a[0] += new[0]
    a[1] += new[1]
    visited.add(tuple(a))
print(len(visited))
