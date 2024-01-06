#!/usr/bin/env python3
from sys import argv

with open(argv[1], 'r') as f:
    lines = f.read().splitlines()

line = lines[0]
floor = 0
for i, c in enumerate(line):
    floor += 1 if c == '(' else -1
    if floor == -1:
        print(i+1)
        exit(0)
