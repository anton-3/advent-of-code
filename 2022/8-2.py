#!/usr/bin/env pypy3
from sys import argv
import math
import re
from pprint import pprint
# CUSTOM LIBRARY FUNCTIONS
from lib import *

lines = readfilelines()
forest = [list(map(int, list(line))) for line in lines]
visible = set()

def listcol(col):
    return [forest[i][col] for i in range(len(forest))]

maxscore = 0
for z in range(len(forest)//2):
    for i, row in enumerate(forest):
        for j, tree in enumerate(row):
            if i == 0 or j == 0 or i == len(forest)-1 or j == len(forest)-1:
                continue
            c = (i, j)
            left = row[:j]
            left.reverse()
            li = 1
            while li < len(left) and left[li-1] < tree:
                li += 1
            right = row[j+1:]
            ri = 1
            while ri < len(right) and right[ri-1] < tree:
                ri += 1
            col = listcol(j)
            up = col[:i]
            up.reverse()
            ui = 1
            while ui < len(up) and up[ui-1] < tree:
                ui += 1
            down = col[i+1:]
            di = 1
            while di < len(down) and down[di-1] < tree:
                di += 1
            score = li * ri * ui * di
#            print(score, c, li, ri, ui, di)
            if score > maxscore:
                maxscore = score

print(maxscore)
