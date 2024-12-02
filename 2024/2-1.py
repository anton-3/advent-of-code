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
    safe = True
    nums = [int(num) for num in line.split()]
    greater = nums[1] > nums[0]
    for i in range(1, len(nums)):
        if greater:
            if nums[i] < nums[i-1]:
                safe = False
                break
        else:
            if nums[i] > nums[i-1]:
                safe = False
                break
        diff = abs(nums[i] - nums[i-1])
        if diff < 1 or diff > 3:
            safe = False
            break
    if safe:
        result += 1
print(result)
