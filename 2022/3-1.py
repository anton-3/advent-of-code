#!/usr/bin/env pypy3
from sys import argv
import math
import re
from pprint import pprint
# CUSTOM LIBRARY FUNCTIONS
from lib import *

lines = readfilelines()
chars = '0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
p = []
for line in lines:
    first, second = line[:len(line)//2], line[len(line)//2:]
    first = [chars.index(i) for i in first]
    second = [chars.index(i) for i in second]
    inter = set(first) & set(second)
    l = list(inter)[0]
    p.append(l)
print(sum(p))
