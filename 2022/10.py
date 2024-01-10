#!/usr/bin/env pypy3
from sys import argv
import math
import re
from pprint import pprint
from itertools import combinations, permutations
# CUSTOM LIBRARY FUNCTIONS
from lib import *

lines = readfilelines()
cycle = 0
x = 1
crt = []

def checkSignal():
    global cycle, x
    cycle += 1
    crt.append('#' if abs((cycle-1) % 40 - x) < 2 else '.')

for line in lines:
    instruction = line.split()[0]
    match instruction:
        case 'noop':
            checkSignal()
        case 'addx':
            num = int(line.split()[1])
            checkSignal()
            checkSignal()
            x += num
            # print(cycle, f'added {num}, new x is {x}, crt: {"".join(crt)}')

for i in range(0, len(crt), 40):
    print(''.join(crt[i:i+40]))
