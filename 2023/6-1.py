#!/usr/bin/env pypy3
from sys import argv
from pprint import pprint
import re

with open(argv[1], 'r') as f:
    lines = f.read().splitlines()

intRegex = '\d+'
intRegexSigned = '-?\d+'

floatRegex = '\d+\.?\d*'
floatRegexSigned = '-?\d+\.?\d*'

defaultSign = False
def reInts(string: str, signed=defaultSign) -> list[int]:
    return list(map(int, re.findall(intRegexSigned if signed else intRegex, string)))

times = reInts(lines[0])
distances = reInts(lines[1])
nums = []
for race in range(len(times)):
    num_ways = 0
    for time in range(times[race]):
        hold_down = time + 1
        if hold_down * (times[race] - hold_down) > distances[race]:
            num_ways += 1
    nums.append(num_ways)
print(nums[0]*nums[1]*nums[2]*nums[3])
