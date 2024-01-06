#!/usr/bin/env python3
from sys import argv

with open(argv[1], 'r') as f:
    lines = f.read().splitlines()

new = 0
literals = 0
for i, line in enumerate(lines):
    literals += len(line)
    new += len(line) + line.count('"') + 2 + line.count('\\')
print(new - literals)
