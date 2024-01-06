#!/usr/bin/env pypy3
from sys import argv
import math
import re
from pprint import pprint
# CUSTOM LIBRARY FUNCTIONS
from lib import *

lines = readfilelines()
line = lines[0]
repeats = 50
for _ in range(repeats):
    nList = []
    cList = []
    i = 0
    while i < len(line):
        c = line[i]
        n = 0
        while i < len(line) and line[i] == c:
            i += 1
            n += 1
        nList.append(n)
        cList.append(c)
    line = ''.join([f'{nList[i]}{cList[i]}' for i in range(len(nList))])
print(len(line))
