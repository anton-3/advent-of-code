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
#    print(a, b, c)

current = 'AAA'
counter = 0
while current != 'ZZZ':
    i = instructions[counter % len(instructions)]
    counter += 1
    current = d[current][1 if i == 'R' else 0]
print(counter)
