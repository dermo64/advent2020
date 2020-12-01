#!/usr/bin/env python

from itertools import combinations
import sys

f = open(sys.argv[1])
input = [int(num) for num in f.readlines()]
pairs = combinations(input,2)
for i in pairs:
    if i[0] + i[1] == 2020:
        print(i[0] * i[1])
        break
