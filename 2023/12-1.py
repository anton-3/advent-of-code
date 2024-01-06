#!/usr/bin/env pypy3
from sys import argv
import math
import re
from pprint import pprint
from itertools import product
# CUSTOM LIBRARY FUNCTIONS
from lib import *

def c(n):
    return [''.join(p) for p in product(['.', '#'], repeat=n)]

def verify(record, nums):
    r = re.split(r'\.+', record)
    if r[-1] == '':
        r.pop()
    if r[0] == '':
        r = r[1:]
#    print(r, nums)
    if len(r) != len(nums):
        return False
    for i, group in enumerate(r):
        if i >= len(nums) or len(group) != nums[i]:
            return False
    return True

lines = readfilelines()
n = 0
for line in lines:
    record, nums = line.split()
    nums = list(map(int, nums.split(',')))
    combs = c(record.count('?'))
    for comb in combs:
#        print(comb)
        s = record
        for char in comb:
            s = s.replace('?', char, 1)
#        print()
        if verify(s, nums):
            n += 1
#            print(s, nums)
print(n)
