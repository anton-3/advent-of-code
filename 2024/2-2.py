#!/usr/bin/env pypy3
from sys import argv
import math
import re
from pprint import pprint
from itertools import combinations, permutations
# CUSTOM LIBRARY FUNCTIONS
from lib import *

lines = readfilelines()
result = 0
for line in lines:
    nums = [int(num) for num in line.split()]
    anysafe = False
    for j in range(len(nums)):
        n = []
        for i in range(len(nums)):
            if i != j:
                n.append(nums[i])

        safe = True
        greater = n[1] > n[0]
        for i in range(1, len(n)):
            if greater:
                if n[i] < n[i-1]:
                    safe = False
                    break
            else:
                if n[i] > n[i-1]:
                    safe = False
                    break
            diff = abs(n[i] - n[i-1])
            if diff < 1 or diff > 3:
                safe = False
                break
        if safe:
            anysafe = True
            break
    if anysafe:
        result += 1
print(result)
