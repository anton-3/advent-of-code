#!/usr/bin/env pypy3
from sys import argv
import math
import re
from pprint import pprint
# CUSTOM LIBRARY FUNCTIONS
from lib import *

lines = readfilelines()

instructions = lines[0]
lines = lines[2:]

d = {}
for line in lines:
    a = line.split()[0]
    b = line.split('(')[1].split(',')[0]
    c = line.split(', ')[-1][:-1]
    d[a] = (b, c)
    #print(a, b, c)

currents = [s for s in d.keys() if s.endswith('A')]
ends_at = {}
counter = 0
c = 0
while len(currents) > 0:
    if c == len(instructions):
        c = 0
    i = instructions[c]
    for current in currents:
        if current[-1] == 'Z':
            currents.remove(current)
            ends_at[current] = counter
            break
    c += 1
    counter += 1
    for j, current in enumerate(currents):
        currents[j] = d[current][1 if i == 'R' else 0]
print(ends_at)
print(math.lcm(*ends_at.values()))
