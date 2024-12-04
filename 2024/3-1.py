#!/usr/bin/env pypy3
from sys import argv
import math
import re
from pprint import pprint
from itertools import combinations, permutations
# CUSTOM LIBRARY FUNCTIONS
from lib import *

line = ''.join(readfilelines())
strings = re.findall(r'mul\(\d{1,3},\d{1,3}\)', line)
result = 0
for string in strings:
    a = int(string.split('(')[1].split(',')[0])
    b = int(string.split(',')[1].split(')')[0])
    result += a * b

print(result)
