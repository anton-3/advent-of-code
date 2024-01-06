#!/usr/bin/env pypy3
from sys import argv
import math
import re
from pprint import pprint
# CUSTOM LIBRARY FUNCTIONS
from lib import *

lines = readfilelines()
l = lines[0].split(', ')
x = y = 0
direction = 0

locations = set()

for thing in l:
    print(locations)
    d = int(thing[1:])
    print(thing, d, x, y)
    match thing[0]:
        case 'L':
            direction = (direction - 1) % 4
        case 'R':
            direction = (direction + 1) % 4
    match direction:
        case 0:
            for i in range(d):
                x -= 1
                coords = (x, y)
                if coords in locations:
                    print(abs(x)+abs(y))
                    exit()
                else:
                    locations.add(coords)
        case 1:
            for i in range(d):
                y += 1
                coords = (x, y)
                if coords in locations:
                    print(abs(x)+abs(y))
                    exit()
                else:
                    locations.add(coords)
        case 2:
            for i in range(d):
                x += 1
                coords = (x, y)
                if coords in locations:
                    print(abs(x)+abs(y))
                    exit()
                else:
                    locations.add(coords)
        case 3:
            for i in range(d):
                y -= 1
                coords = (x, y)
                if coords in locations:
                    print(abs(x)+abs(y))
                    exit()
                else:
                    locations.add(coords)
print(x+y)
