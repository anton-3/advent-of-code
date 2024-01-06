from sys import argv
import re
from os import linesep

int_regex = '\d+'
int_regex_signed = '-?\d+'

float_regex = '\d+\.?\d*'
float_regex_signed = '-?\d+\.?\d*'

def readfile(filename=argv[1] if len(argv) > 1 else 'test.txt'):
    with open(filename, 'r') as f:
        return f.read()

def readfilelines(filename=argv[1] if len(argv) > 1 else 'test.txt'):
    return readfile(filename).splitlines()

def readfilechunks(filename=argv[1] if len(argv) > 1 else 'test.txt'):
    return [chunk.splitlines() for chunk in readfile(filename).split(linesep * 2)]

def readint(string: str, signed=False) -> int:
    result = re.search(int_regex_signed if signed else int_regex, string)
    return int(result.group(0)) if result else None

def readints(string: str, signed=False) -> list[int]:
    return list(map(int, re.findall(int_regex_signed if signed else int_regex, string)))

def readints2d(string: str, signed=False) -> list[list[int]]:
    arr = []
    for line in string.splitlines():
        arr.append(readints(line, signed))
    return arr

def readfloat(string: str, signed=False) -> float:
    result = re.search(float_regex_signed if signed else float_regex, string)
    return float(result.group(0)) if result else None

def readfloats(string: str, signed=False) -> list[float]:
    return list(map(float, re.findall(float_regex_signed if signed else float_regex, string)))

def readfloats2d(string: str, signed=False) -> list[list[float]]:
    arr = []
    for line in string.splitlines():
        arr.append(readfloats(line, signed))
    return arr
