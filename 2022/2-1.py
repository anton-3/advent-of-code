#!/usr/bin/env pypy3
from sys import argv
import math
import re
from pprint import pprint
# CUSTOM LIBRARY FUNCTIONS
from lib import *

lines = readfilelines()
m = {'A': 'rock', 'B': 'paper', 'C': 'scissors', 'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}
scores = {'rock': 1, 'paper': 2, 'scissors': 3}
total = 0
for line in lines:
    opp, you = line.split()
    opp = m[opp]
    you = m[you]
    score = scores[you]
    if opp == you:
        score += 3
    elif opp == 'rock' and you == 'paper' or opp == 'paper' and you == 'scissors' or opp == 'scissors' and you == 'rock':
        score += 6
    total += score
print(total)
