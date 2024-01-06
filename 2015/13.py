#!/usr/bin/env pypy3
from sys import argv
import math
import re
from pprint import pprint
from itertools import combinations, permutations
# CUSTOM LIBRARY FUNCTIONS
from lib import *

lines = readfilelines()
happy = {}
for line in lines:
    s = line[:-1].split()
    person1 = s[0]
    person2 = s[-1]
    num = int(s[3])
    if s[2] == 'lose':
        num = -num
    if person1 not in happy:
        happy[person1] = {}
    happy[person1][person2] = num

people = list(happy.keys())
happy['me'] = {}
for person in people:
    happy['me'][person] = 0
    happy[person]['me'] = 0
people.append('me')
numPeople = len(people)
maxHappiness = -1
for permutation in list(permutations(people)):
    happiness = 0
    for i in range(numPeople):
        person = permutation[i]
        leftPerson = permutation[i-1]
        rightPerson = permutation[i+1 if i+1 < numPeople else 0]
        happiness += happy[person][leftPerson]
        happiness += happy[person][rightPerson]
    maxHappiness = max(maxHappiness, happiness)
print(maxHappiness)
