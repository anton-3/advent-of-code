#!/usr/bin/env pypy3
from sys import argv
import math
import re
from pprint import pprint
# CUSTOM LIBRARY FUNCTIONS
from lib import *

start, instructions = [x.splitlines() for x in readfile().split('\n\n')]
stacknums = readints(start[-1])
stacks = [[] for i in range(len(stacknums))]
for i in stacknums:
    idx = 4 * i - 3
    for j in range(len(start)-1):
        if idx < len(start[j]) and start[j][idx] != ' ':
            stacks[i-1].append(start[j][idx])
stacks = [list(reversed(s)) for s in stacks]
pprint(stacks)

for line in instructions:
    move, from_, to = readints(line)
    for i in range(move):
        stacks[to-1].append(stacks[from_ - 1].pop())
print(''.join([s[-1] for s in stacks]))
