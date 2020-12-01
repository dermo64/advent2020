#!/usr/bin/env python

from itertools import combinations
from math import prod
import sys

with open(sys.argv[1]) as f:
    input = [int(num) for num in f.readlines()]
    tups = combinations(input, int(sys.argv[2]))
    for i in tups:
        if sum(i) == 2020:
            print(prod(i))
            break
