#!/usr/bin/env pypy3
from collections import deque
from itertools import combinations
from copy import deepcopy

def printLocations(locations: list):
    for i, floor in enumerate(locations):
        j = 4-i-1
        print(f'F{j+1} - {" ".join(locations[j])}')

# def getNeighbors(floor: int, microchips: list, generators: list, steps: int) -> list:
def getNeighbors(currentFloor: int, locations: list, steps: int) -> list:
    neighbors = []
    things = locations[currentFloor]
    carryable = set(things)
    if len(things) > 1:
        carryable |= set(combinations(things, 2))
    # for c in deepcopy(carryable):
    #     if isinstance(c, tuple) and c[0][1] != c[1][1] and c[0][0] != c[1][0]:
    #         carryable.remove(c)
    neighborFloors = []
    if currentFloor > 0: neighborFloors.append(currentFloor-1)
    if currentFloor < 3: neighborFloors.append(currentFloor+1)
    neighbors = []
    for c in carryable:
        for f in neighborFloors:
            newLocations = deepcopy(locations)
            if isinstance(c, tuple):
                for thing in c:
                    newLocations[currentFloor].remove(thing)
                    newLocations[f].append(thing)
            else:
                newLocations[currentFloor].remove(c)
                newLocations[f].append(c)
            validNeighbor = True
            for floor in newLocations:
                for thing in floor:
                    if thing[1] == 'M' and f'{thing[0]}G' not in floor and len([t for t in floor if t[1] == 'G']) > 0:
                        validNeighbor = False
                        break
            if validNeighbor:
                neighbors.append((f, newLocations, steps+1))
    return neighbors

def checkGoal(locations: list) -> bool:
    return len(locations[0] + locations[1] + locations[2]) == 0

def makeHashable(bfsNode: tuple):
    floor, locations, steps = bfsNode
    hashableLocations = tuple([tuple(sorted(floor)) for floor in locations])
    return (floor, hashableLocations)

def bfs(startLocations: list) -> int:
    queue = deque()
    visited = set()
    start = (0, startLocations, 0)
    queue.appendleft(start)
    visited.add(makeHashable(start))
    iterations = 0

    while queue:
        current = queue.pop()
        floor, locations, steps = current
        if checkGoal(locations):
            return steps
        neighbors = getNeighbors(floor, locations, steps)
        for neighbor in neighbors:
            if makeHashable(neighbor) not in visited:
                queue.appendleft(neighbor)
                visited.add(makeHashable(neighbor))
    return iterations

# locations = [['HM', 'LM'], ['HG'], ['LG'], []]
# locations = [['SG', 'SM', 'PG', 'PM'], ['TG', 'RG', 'RM', 'CG', 'CM'], ['TM'], []]
locations = [['SG', 'SM', 'PG', 'PM', 'EG', 'EM', 'DG', 'DM'], ['TG', 'RG', 'RM', 'CG', 'CM'], ['TM'], []]
printLocations(locations)

minimumSteps = bfs(locations)
print(minimumSteps)
