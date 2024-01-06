#!/usr/bin/env pypy3
import math
import re
from pprint import pprint
# CUSTOM LIBRARY FUNCTIONS
from lib import *

f=lambda n:0 if set(n)=={0} else n[-1]+f([b-a for a,b in zip(n,n[1:])])
print(sum(f(readints(line,True)) for line in readfilelines()))
print(sum(f(readints(line,True)[::-1]) for line in readfilelines()))
