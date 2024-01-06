#!/usr/bin/env python3
from sys import argv

with open(argv[1], 'r') as f:
    lines = f.read().splitlines()

area = 0
for line in lines:
    l,w,h = sorted(map(int, line.split('x')))
    area += 2*(l+w) + l*w*h
print(area)
