#!/usr/bin/env python

from itertools import combinations
import sys

f = open(sys.argv[1])
input = [int(num) for num in f.readlines()]
trips = combinations(input,3)
for i in trips:
    if i[0] + i[1] + i[2] == 2020:
        print(i[0] * i[1] * i[2])
        break
