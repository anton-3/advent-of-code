#!/usr/bin/env python3
# THIS DOESN'T WORK (FUCK THIS ONE)
from sys import argv
from pprint import pprint

with open(argv[1], 'r') as f:
    lines = f.read().rstrip().splitlines()

d = {}
for line in lines:
    left, right = line.split(' -> ')
    d[right] = left

def get(key):
#    print(f'getting value for {key}')
    if key.isdigit():
        return int(key)
    left = d[key].split(' ')

    if len(left) == 1:
        return get(left[0])
    elif len(left) == 2:
        return 0b1111111111111111 - get(left[1])
    elif len(left) == 3:
        a, b = left[0], left[2]
        if left[1] == 'AND':
            return get(a) & get(b)
        elif left[1] == 'OR':
            return get(a) | get(b)
        elif left[1] == 'LSHIFT':
            return get(a) << get(b)
        elif left[1] == 'RSHIFT':
            return get(a) >> get(b)
pprint(d)
print(get('b'))
#pprint([(k, get(k)) for k in d.keys()])
