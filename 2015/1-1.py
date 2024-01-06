#!/usr/bin/env python3
from sys import argv

with open(argv[1], 'r') as f:
    lines = f.read().splitlines()

line = lines[0]
floor = 0
for c in line:
    floor += 1 if c == '(' else -1
print(floor)
