#!/usr/bin/env python3
from sys import argv
from pprint import pprint

with open(argv[1], 'r') as f:
    lines = f.read().splitlines()

seed_numbers = [int(x) for x in lines[0].split(': ')[1].split()]
seed_ranges = []
for i in range(len(seed_numbers)//2):
    seed_ranges.append(range(seed_numbers[2*i], seed_numbers[2*i] + seed_numbers[2*i+1]))

lines = ['EMPTYLINE' if line == '' else line for line in lines[2:]]
maps = [x.split('\n')[1:] for x in '\n'.join(lines).split('\nEMPTYLINE\n')]

for location in range(100000000):
    seed = location
    for m in reversed(maps):
        for line in m:
            a, b, c = [int(x) for x in line.split()]
            if seed in range(a, a+c):
                seed += b - a
                break
    for r in seed_ranges:
        if seed in r:
            print(location, seed)
            exit()
