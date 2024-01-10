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
importantCycles = {20, 60, 100, 140, 180, 220}
signalStrengths = []

def checkSignal():
    global cycle, x, importantCycles, signalStrengths
    print(cycle, x)
    cycle += 1
    if cycle not in importantCycles:
        return
    signalStrengths.append(cycle * x)

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
print(signalStrengths)
print(sum(signalStrengths))

# 11080
