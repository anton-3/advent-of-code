#!/usr/bin/env pypy3
from sys import argv
import math
import re
from pprint import pprint
from functools import cmp_to_key
# CUSTOM LIBRARY FUNCTIONS
from lib import *

cards = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7, 'T': 8, 'J': -1, 'Q': 10, 'K': 11, 'A': 12}

# five of a kind > four > full house > three > two pair > one pair > high card

lines = readfilelines()
five = set()
four = set()
full = set()
three = set()
two = set()
one = set()
high = set()
hands = []
bids = []
for i, line in enumerate(lines):
    hand, bid = line.split()
    print(f'{i}: evaluating {hand}')
    bid = int(bid)
    hand = list(hand)
    hands.append(hand)
    bids.append(bid)
    s_hand = set(hand)
    if 'J' in s_hand:
        max_rank = 0
        for card in cards.keys():
            rank = 1
            new_hand = [card if c == 'J' else c for c in hand]
            s_hand = set(new_hand)
            #print(s_hand)
            if len(s_hand) == 1:
                rank = 7
            elif len(s_hand) == 2:
                for card in cards.keys():
                    c = new_hand.count(card)
                    if c == 4:
                        rank = 6
                        break
                    elif c == 3:
                        rank = 5
                        break
            elif len(s_hand) == 3:
                for card in cards.keys():
                    c = new_hand.count(card)
                    if c == 3:
                        rank = 4
                        break
                    elif c == 2:
                        rank = 3
                        break
            elif len(s_hand) == 4:
                rank = 2
            #print(f'card={card}, rank={rank}')
            max_rank = max(max_rank, rank)
        if max_rank == 7:
            five.add(i)
        elif max_rank == 6:
            four.add(i)
        elif max_rank == 5:
            full.add(i)
        elif max_rank == 4:
            three.add(i)
        elif max_rank == 3:
            two.add(i)
        elif max_rank == 2:
            one.add(i)
        else:
            high.add(i)

    else:
        if len(s_hand) == 1:
            five.add(i)
        elif len(s_hand) == 2:
            for card in cards.keys():
                c = hand.count(card)
                if c == 4:
                    four.add(i)
                    break
                elif c == 3:
                    full.add(i)
                    break
        elif len(s_hand) == 3:
            for card in cards.keys():
                c = hand.count(card)
                if c == 3:
                    three.add(i)
                    break
                elif c == 2:
                    two.add(i)
                    break
        elif len(s_hand) == 4:
            one.add(i)
        else:
            high.add(i)

everything = [five, four, full, three, two, one, high]
everything = [list(e) for e in everything]
for e in everything:
    for i in range(5):
        e.sort(key=lambda x: [cards[c] for c in hands[x]][4-i], reverse=True)
final = sum(everything, [])
result = 0
for i, f in enumerate(final):
    h = ''.join(hands[f])
    t = 'five' if f in five else 'four' if f in four else 'full' if f in full else 'three' if f in three else 'two' if f in two else 'one' if f in one else 'high'
    rank = len(final) - i
    print(f'rank {rank} {h}: {t}')
    result += rank * bids[f]
print(result)
