#!/usr/bin/env pypy3
from sys import argv
import math
import re
from pprint import pprint
# CUSTOM LIBRARY FUNCTIONS
from lib import *
import json

def count(data):
    if isinstance(data, str):
        return 0
    if isinstance(data, int):
        return data
    if isinstance(data, list):
        return sum([count(d) for d in data])
    if isinstance(data, dict):
        values = data.values()
        if 'red' in values:
            return 0
        return sum([count(d) for d in values])
    print('WHAT THE FUCK')

lines = readfilelines()
print(sum(readints(lines[0], signed=True)))
data = json.loads(lines[0])
print(count(data))

# 126674 HIGH
