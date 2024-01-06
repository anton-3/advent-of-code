#!/usr/bin/env python3
from sys import argv

with open(argv[1], 'r') as f:
    lines = f.read().splitlines()

literals = 0
memory = 0
for i, line in enumerate(lines):
    print('=====', i, '=====')
    print(len(line), line)
    literals += len(line)
    memory += len(eval(line))
    line = line[1:-1]
    line = line.replace('\\\\', '\\')
    line = line.replace('\\x', 'FUCK')
    line = line.replace('\\"', '"')
    line = line.replace("\\'", "'")
    print(len(line) - 5 * line.count('FUCK'), line)
    #memory += len(line) - 5 * line.count('FUCK')
print(literals - memory)
