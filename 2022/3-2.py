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
for i in range(len(lines)//3):
    a, b, c = lines[3*i], lines[3*i+1], lines[3*i+2]
    a = set([chars.index(i) for i in a])
    b = set([chars.index(i) for i in b])
    c = set([chars.index(i) for i in c])
    inter = a & b & c
    l = list(inter)[0]
    p.append(l)
print(sum(p))
