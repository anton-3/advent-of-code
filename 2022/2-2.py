#!/usr/bin/env pypy3
from sys import argv
import math
import re
from pprint import pprint
# CUSTOM LIBRARY FUNCTIONS
from lib import *

lines = readfilelines()
m = {'A': 'rock', 'B': 'paper', 'C': 'scissors'}
scores = {'rock': 1, 'paper': 2, 'scissors': 3}
total = 0
for line in lines:
    opp, wl = line.split()
    opp = m[opp]
    you = None
    score = None
    if wl == 'X':
        score = 0 + scores['rock' if opp == 'paper' else 'paper' if opp == 'scissors' else 'scissors']
    elif wl == 'Y':
        score = 3 + scores[opp]
    else:
        score = 6 + scores['rock' if opp == 'scissors' else 'scissors' if opp == 'paper' else 'paper']
    total += score
print(total)
