#!/usr/bin/env pypy3
from sys import argv
import math
import re
from pprint import pprint
# CUSTOM LIBRARY FUNCTIONS
from lib import *

lines = readfilelines()
total = 0
for line in lines:
    f1, f2, s1, s2 = readints(line)
    if set(range(f1, f2+1)) & set(range(s1, s2+1)):
        total += 1
print(total)
