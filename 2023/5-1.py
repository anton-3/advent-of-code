#!/usr/bin/env python3
from sys import argv

with open(argv[1], 'r') as f:
    lines = f.read().splitlines()

seeds = [int(x) for x in lines[0].split(': ')[1].split()]

lines = ['EMPTYLINE' if line == '' else line for line in lines[2:]]
maps = [x.split('\n')[1:] for x in '\n'.join(lines).split('\nEMPTYLINE\n')]

for m in maps:
    mapped = seeds.copy()
    for line in m:
        a, b, c = [int(x) for x in line.split()]
        destrange = range(a, a+c)
        sourcerange = range(b, b+c)
        for i, seed in enumerate(seeds):
            if seed in sourcerange:
                mapped[i] += a - b
    seeds = mapped
print(sorted(seeds))
