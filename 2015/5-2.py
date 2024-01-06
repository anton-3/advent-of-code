#!/usr/bin/env python3
from sys import argv

with open(argv[1], 'r') as f:
    lines = f.read().splitlines()

nice = 0
for line in lines:
    pairs = [f'{c}{line[i+1]}' for i, c in enumerate(line[:-1])]
    pair_check = False
    for pair in pairs:
        if pair in line.replace(pair, '-', 1):
            pair_check = True
    repeat_check = False
    for i, c in enumerate(line[:-2]):
        if c == line[i+2]:
            repeat_check = True
    if pair_check and repeat_check:
        nice += 1
print(nice)
