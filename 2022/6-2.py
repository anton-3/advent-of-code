#!/usr/bin/env pypy3
from sys import argv
import math
import re
from pprint import pprint
# CUSTOM LIBRARY FUNCTIONS
from lib import *

line = readfile()
for i, c in enumerate(line[:-4]):
    sub = line[i:i+14]
    if len(set(sub)) == 14:
        print(i+14)
        exit()
