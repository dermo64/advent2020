#!/usr/bin/env python

from itertools import combinations
from math import prod
import sys

def num_trees(input, move):
    count = 0
    row, column = 0, 0
    while row < len(input):
        if input[row][column % len(input[row])] == '#':
            count += 1
        row  += move[0]
        column += move[1]
    return count


with open(sys.argv[1]) as f:
    input = [list(line.strip()) for line in f.readlines()]
 
        
print(num_trees(input, (1,3)))

moves = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]

print(prod([num_trees(input, move) for move in moves]))