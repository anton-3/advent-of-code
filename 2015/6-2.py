#!/usr/bin/env python3
from sys import argv
from pprint import pprint

with open(argv[1], 'r') as f:
    lines = f.read().splitlines()

grid = [[0] * 1000 for i in range(1000)]
for line in lines:
    words = line.split()
    start_x, start_y = [int(x) for x in words[2 if words[0] == 'turn' else 1].split(',')]
    end_x, end_y = [int(x) for x in words[-1].split(',')]
    print(line)
    print(start_x, start_y, end_x, end_y)
    for i in range(start_x, end_x+1):
        for j in range(start_y, end_y+1):
            if line.startswith('turn on'):
                grid[i][j] += 1
            elif line.startswith('turn off'):
                grid[i][j] = max(0, grid[i][j]-1)
            else:
                grid[i][j] += 2
print(sum([sum(row) for row in grid]))
