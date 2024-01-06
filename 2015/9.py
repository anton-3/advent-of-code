#!/usr/bin/env pypy3
from sys import argv
import math
import re
from pprint import pprint
from collections import deque
# CUSTOM LIBRARY FUNCTIONS
from lib import *
from itertools import permutations

lines = readfilelines()

graph = {}
for line in lines:
    l1, _, l2, _, distance = line.split()
    for l in l1, l2:
        if l not in graph:
            graph[l] = {}
    graph[l1][l2] = int(distance)
    graph[l2][l1] = int(distance)

min_distance = float('inf')
max_distance = 0
locations = set(graph)
n = len(locations)
for permutation in list(permutations(locations)):
    distance = 0
    for i in range(n-1):
        l1 = permutation[i]
        l2 = permutation[i+1]
        distance += graph[l1][l2]
    min_distance = min(min_distance, distance)
    max_distance = max(max_distance, distance)
print(f'minimum distance: {min_distance}')
print(f'maximum distance: {max_distance}')
