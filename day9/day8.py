#!/usr/bin/env python
import sys
from itertools import combinations

def find_invalid(N):
    for i in range(N,len(program)):
        if program[i] not in [pair[0] + pair[1] for pair in combinations(program[i-N:i],2)]:
            return program[i]
    return 0

def find_weakness(num, program):
  #  print(num)
    for i in range(0,len(program)):
        for j in range(i,len(program)):
            slice = program[i:j]
            if sum(slice) == num:
                return min(slice) + max(slice)
                

with open(sys.argv[1]) as f:
    program = [int(line.strip()) for line in f]

    invalid_number = find_invalid(25)
    print(invalid_number)

    print(find_weakness(invalid_number, program))







