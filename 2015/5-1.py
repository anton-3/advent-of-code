#!/usr/bin/env python3
from sys import argv

with open(argv[1], 'r') as f:
    lines = f.read().splitlines()

nice = 0
for line in lines:
    vowel_check = len([c for c in line if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u']) >= 3
    double_check = False
    for i, c in enumerate(line[:-1]):
        if c == line[i+1]:
            double_check = True
    strings_check = 'ab' not in line and 'cd' not in line and 'pq' not in line and 'xy' not in line
    if vowel_check and double_check and strings_check:
        nice += 1
print(nice)
