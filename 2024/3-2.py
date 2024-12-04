#!/usr/bin/env pypy3
from sys import argv
import math
import re
from pprint import pprint
from itertools import combinations, permutations
# CUSTOM LIBRARY FUNCTIONS
from lib import *

line = ''.join(readfilelines())
strings = re.finditer(r'mul\(\d{1,3},\d{1,3}\)', line)
result = 0
dos = set(match.start() for match in re.finditer(r'do\(\)', line))
donts = set(match.start() for match in re.finditer(r'don\'t\(\)', line))
for match in strings:
    string = match.group()
    index = match.start()
    do = True
    for i in reversed(range(index)):
        if i in dos:
            break
        if i in donts:
            do = False
            break
    if do:
        a = int(string.split('(')[1].split(',')[0])
        b = int(string.split(',')[1].split(')')[0])
        result += a * b

print(result)
