#!/usr/bin/env pypy3
from sys import argv
import math
import re
from pprint import pprint
from time import sleep
# CUSTOM LIBRARY FUNCTIONS
from lib import *

def bitCount(n):
    count = 0
    while n:
        n &= n-1
        count += 1
    return count

def getNeighbors(v):
    global grid
    (i, j) = v
    neighbors = [(i+1,j), (i,j+1), (i-1,j), (i,j-1)]
    return {n for n in neighbors if n[0]>=0 and n[1]>=0 and n[0]<50 and n[1]<50 and not grid[n[0]][n[1]]}

def printGrid():
    global grid
    global path
    global size
    p = []
    for i in range(size):
        p.append([])
        for j in range(size):
            p[i].append('#' if grid[i][j] else 'O' if (i, j) in path else ' ')
    print('='*size)
    print('\n'.join([''.join(z) for z in p]))

n = 1364
size = 50
grid = []
for i in range(size):
    grid.append([])
    for j in range(size):
        m = i*i + 3*i + 2*i*j + j + j*j + n
        b = bitCount(m)
        grid[i].append(b % 2 == 1)

unvisited = set()
distances = {}
for i in range(size):
    for j in range(size):
        if grid[i][j]:
            continue
        c = (i, j)
        unvisited.add(c)
        distances[c] = 9999
start = (1, 1)
distances[start] = 0
path = set()

for i in range(len(unvisited)):
    minV = None
    minDistance = 9999
    for u in unvisited:
        if distances[u] < minDistance:
            minV = u
            minDistance = distances[u]
    path.add(minV)
    unvisited.remove(minV)

    printGrid()
    sleep(0.1)

    allNeighbors = set()
    for v in path:
        allNeighbors |= getNeighbors(v)
    for v in path:
        if v in allNeighbors:
            allNeighbors.remove(v)
    if not allNeighbors:
        break

    for u in allNeighbors:
        if distances[u] > minDistance+1:
            distances[u] = minDistance+1

goal = (31, 39)
maxDistance = 50
print(f'Distance to goal square {goal}: {distances[goal]}')
print(f'Number of squares within max distance {maxDistance}: {len({p for p in path if distances[p] <= maxDistance})}')
