#!/usr/bin/env pypy3
from sys import argv
import math
import re
from pprint import pprint
# CUSTOM LIBRARY FUNCTIONS
from lib import *

file = readfile().split('\n\n')
chunks = [list(map(int, chunk.strip().split('\n'))) for chunk in file]
sums = [sum(chunk) for chunk in chunks]
sums.sort()
print(sums[-1])
print(sums[-2]+sums[-1]+sums[-3])
