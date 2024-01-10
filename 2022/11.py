#!/usr/bin/env pypy3
from sys import argv
import math
import re
from pprint import pprint
from itertools import combinations, permutations
# CUSTOM LIBRARY FUNCTIONS
from lib import *

monkeysInput = readfilechunks()

monkeyItems = []
operations = []
operands = []
tests = []
throws = []
for monkey in monkeysInput:
    monkeyItems.append([{i} for i in readints(monkey[1])])
    operation, operand = monkey[2].split()[-2:]
    operations.append(operation)
    operands.append(operand)
    tests.append(readints(monkey[3])[0])
    trueThrow = readints(monkey[4])[0]
    falseThrow = readints(monkey[5])[0]
    throws.append((trueThrow, falseThrow))

numRounds = 20
numMonkeys = len(monkeysInput)
numInspections = [0] * numMonkeys
for i in range(numRounds):
    for j in range(numMonkeys):
        items = monkeyItems[j]
        numInspections[j] += len(items)
        for item in items:
            worryLevel = item
            if operations[j] == '+':
                if operands[j] == 'old':
                    worryLevel += item
                else:
                    worryLevel += int(operands[j])
            else:
                if operands[j] == 'old':
                    worryLevel *= item
                else:
                    worryLevel *= int(operands[j])
            test = worryLevel % tests[j] == 0
            recipientMonkey = throws[j][0] if test else throws[j][1]
            monkeyItems[recipientMonkey].append(worryLevel)
        items.clear()

print(numInspections)
numInspections.sort()
monkeyBusiness = numInspections[-2] * numInspections[-1]
print(monkeyBusiness)
