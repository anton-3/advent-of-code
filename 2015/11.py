#!/usr/bin/env pypy3
from sys import argv
import math
import re
from pprint import pprint
# CUSTOM LIBRARY FUNCTIONS
from lib import *

def convert(string):
    return [ord(letter) - 97 for letter in string]

def convertBack(string):
    return ''.join([chr(number + 97) for number in string])

lines = readfilelines()
# lines[0] = 'vzbxxyzz'
password = convert(lines[0])

disallowedLetters = set(convert('iol'))
def checkValid(password):
    valid = False
    for i in range(len(password)-2):
        if password[i] in disallowedLetters:
            return False
        if password[i]+1 == password[i+1] and password[i+1]+1 == password[i+2]:
            valid = True
    if not valid:
        return False
    if password[-2] in disallowedLetters or password[-1] in disallowedLetters:
        return False
    pairs = [(password[i], password[i+1]) for i in range(len(password)-1)]
    repeatPairs = {pair for pair in pairs if pair[0] == pair[1]}
    return len(repeatPairs) >= 2

def increment(password):
    i = len(password)-1
    password[i] += 1
    while password[i] == 26:
        password[i] = 0
        i -= 1
        password[i] += 1
    for i in range(len(password)):
        if password[i] in disallowedLetters:
            password[i] += 1

# increment(password)
while not checkValid(password):
    increment(password)
print(convertBack(password))
