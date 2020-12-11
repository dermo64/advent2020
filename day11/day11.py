#!/usr/bin/env python
import sys
import copy

def get_occupied_pt1(data, row, col):
    occupied = 0
    if row != 0:
        if col != 0 and data[row - 1][col - 1] == '#':
            occupied += 1
        if data[row - 1][col] == '#':
            occupied += 1
        if col != len(data[0]) - 1 and data[row - 1][col + 1] == '#':
            occupied += 1
    if col != 0 and data[row][col - 1] == '#':
        occupied += 1
    if col != len(data[0]) - 1 and data[row][col + 1] == '#':
        occupied += 1
    if row != len(data) - 1:
        if col != 0 and data[row + 1][col - 1] == '#':
            occupied += 1
        if data[row + 1][col] == '#':
            occupied += 1
        if col != len(data[0]) - 1 and data[row + 1][col + 1] == '#':
            occupied += 1
    return occupied

def get_occupied_pt2(data, row, col):
    occupied = 0
    for i in range(col - 1, -1, -1):
        if(data[row][i]) == '#':
            occupied += 1
            break
        if(data[row][i]) == 'L':
            break
    for i in range(col + 1, len(data[0])):
        if(data[row][i]) == '#':
            occupied += 1
            break
        if(data[row][i]) == 'L':
            break
    for i in range(row - 1, -1, -1):
        if(data[i][col]) == '#':
            occupied += 1
            break
        if(data[i][col]) == 'L':
            break
    for i in range(row + 1, len(data)):
        if(data[i][col]) == '#':
            occupied += 1
            break
        if(data[i][col]) == 'L':
            break
    for (i, j) in zip(range(col - 1, -1, -1), range(row - 1, -1, -1)):
        if(data[j][i]) == '#':
            occupied += 1
            break
        if(data[j][i]) == 'L':
            break
    for (i, j) in zip(range(col - 1, -1, -1), range(row + 1, len(data))):
        if(data[j][i]) == '#':
            occupied += 1
            break
        if(data[j][i]) == 'L':
            break
    for (i, j) in zip(range(col + 1, len(data[0])), range(row - 1, -1, -1)):
        if(data[j][i]) == '#':
            occupied += 1
            break
        if(data[j][i]) == 'L':
            break   
    for (i, j) in zip(range(col + 1, len(data[0])), range(row + 1, len(data))):        
        if(data[j][i]) == '#':
            occupied += 1
            break
        if(data[j][i]) == 'L':
            break
    return occupied

def get_num_occupied(data, part):
    swaps = True
    threshold = 4 if part == 1 else 5
    while swaps:
        swaps = 0
        snapshot = copy.deepcopy(data)
        for row in range(0, len(data)):
            for col in range(0, len(data[0])):
                occupied = get_occupied_pt1(data, row, col) if part == 1 else get_occupied_pt2(data, row, col)                 
                if data[row][col] == 'L' and occupied == 0:
                    snapshot[row][col] = '#'
                    swaps = True
                elif data[row][col] == '#' and occupied >= threshold:
                    snapshot[row][col] = 'L'
                    swaps = True
        data = snapshot
    return sum([line.count('#') for line in data])

with open(sys.argv[1]) as f:
    input = [[char for char in line.strip()] for line in f]
    print(get_num_occupied(copy.deepcopy(input), 1))
    print(get_num_occupied(copy.deepcopy(input), 2))



