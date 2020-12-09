#!/usr/bin/env python
import sys
from itertools import combinations

def find_invalid(data, N):
    for i in range(N,len(data)):
        if data[i] not in [pair[0] + pair[1] for pair in combinations(data[i-N:i],2)]:
            return data[i]

def find_weakness(num, data):
    for i in range(0,len(data)):
        for j in range(i,len(data)):
            slice = data[i:j]
            if sum(slice) == num:
                return min(slice) + max(slice)
                
with open(sys.argv[1]) as f:
    data = [int(line.strip()) for line in f]
    invalid_number = find_invalid(data, 25)
    #Part 1
    print(invalid_number)
    #Part 2
    print(find_weakness(invalid_number, data))







