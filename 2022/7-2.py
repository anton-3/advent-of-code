#!/usr/bin/env pypy3
from sys import argv
import math
import re
from pprint import pprint
# CUSTOM LIBRARY FUNCTIONS
from lib import *

lines = readfilelines()[2:]
pwd = ['']
files = {}
dirs = {'/'}
for line in lines:
    if line.startswith('$ cd'):
        d = line.split()[-1]
        if d == '..':
            pwd.pop()
        else:
            pwd.append(d)
            dirs.add('/'.join(pwd))
        print(f'pwd: {pwd}')
    elif line.startswith('$ ls'):
        pass
    else:
        size, filename = line.split()
        if size == 'dir':
            continue
        size = int(size)
        filepath = f'{"/".join(pwd)}/{filename}'
        files[filepath] = size
print(dirs)
pprint(files)
result = 0

dirsizes = {}
for d in dirs:
    size = 0
    for filepath in files.keys():
        if filepath.startswith(d + '/'):
            size += files[filepath]
    dirsizes[d] = size
dirsizes['/'] = sum(files.values())
print('dirsizes')
pprint(dirsizes)
print(min([dirsizes[d] for d in dirsizes.keys() if dirsizes['/'] - dirsizes[d] <= 40000000]))
