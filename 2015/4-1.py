#!/usr/bin/env python3
from sys import argv
import hashlib

with open(argv[1], 'r') as f:
    key = f.read().strip()

i = 0
h = ''
while not h.startswith('00000'):
    i += 1
    h = hashlib.md5(bytes(key+str(i), 'utf-8')).hexdigest()
print(i, h)
