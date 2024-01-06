#!/usr/bin/env pypy3
from sys import argv
from pprint import pprint
import re
import math

with open(argv[1], 'r') as f:
    lines = f.read().splitlines()

intRegex = '\d+'
intRegexSigned = '-?\d+'

floatRegex = '\d+\.?\d*'
floatRegexSigned = '-?\d+\.?\d*'

defaultSign = False
def reInts(string: str, signed=defaultSign) -> list[int]:
    return list(map(int, re.findall(intRegexSigned if signed else intRegex, string)))

time = int(''.join([str(i) for i in reInts(lines[0])]))
distance = int(''.join([str(i) for i in reInts(lines[1])]))
print(time, distance)
lower = None
upper = None
for t in range(time):
    hold_down = t + 1
    if hold_down * (time - hold_down) > distance:
        lower = t+1
        break
for t in range(time):
    hold_down = time-t
    if hold_down * (time - hold_down) > distance:
        upper = time-t
        break
print(upper, lower, upper-lower+1)
