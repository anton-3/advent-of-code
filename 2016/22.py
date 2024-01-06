#!/usr/bin/env pypy3
from sys import argv
import math
import re
from pprint import pprint
from collections import deque
from time import sleep
# CUSTOM LIBRARY FUNCTIONS
from lib import *

lines = readfilelines()

sizeX, sizeY = [a+1 for a in readints(lines[-1])[:2]]
# index this with Y value, X value
usage = [[0] * sizeX for _ in range(sizeY)]

for line in lines[2:]:
    ints = readints(line)
    x = ints[0]
    y = ints[1]
    used = ints[3]
    usage[y][x] = used

# there is only one empty node in the grid
emptyX = None
emptyY = None
# there are several "big nodes" which need to be avoided in the BFS
bigNodes = set()

avgUsage = sum([sum(row) for row in usage]) / (sizeX * sizeY)
for y, row in enumerate(usage):
    for x, used in enumerate(row):
        if used == 0:
            emptyX, emptyY = x, y
        elif used > 2 * avgUsage:
            bigNodes.add((x, y))

def bfs(dataNode, goalNode, emptyNode, bigNodes):
    global sizeX, sizeY
    dataStartX, dataStartY = dataNode
    emptyStartX, emptyStartY = emptyNode
    goalX, goalY = goalNode
    directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
    start = (dataStartX, dataStartY, emptyStartX, emptyStartY, 0)
    queue = deque([start])
    visited = {start[:-1]}
    while queue:
        dataX, dataY, emptyX, emptyY, steps = queue.popleft()
        if dataX == goalX and dataY == goalY:
            return steps
        for dx, dy in directions:
            newEmptyX = emptyX + dx
            newEmptyY = emptyY + dy
            if newEmptyX < 0 or newEmptyY < 0 or newEmptyX >= sizeX or newEmptyY >= sizeY:
                continue
            if (newEmptyX, newEmptyY) in bigNodes:
                continue
            newDataX = None
            newDataY = None
            if newEmptyX == dataX and newEmptyY == dataY:
                newDataX, newDataY = emptyX, emptyY
            else:
                newDataX, newDataY = dataX, dataY
            nextState = (newDataX, newDataY, newEmptyX, newEmptyY, steps+1)
            nextStateWithoutSteps = nextState[:-1]
            if nextStateWithoutSteps not in visited:
                queue.append(nextState)
                visited.add(nextStateWithoutSteps)

dataNode = (sizeX - 1, 0)
goalNode = (0, 0)
emptyNode = (emptyX, emptyY)
steps = bfs(dataNode, goalNode, emptyNode, bigNodes)
print(steps)

# 209 LOW
