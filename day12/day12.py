#!/usr/bin/env python
import sys

def move(pos, dir, num):
    if dir in ['E', 'N']:
        pos[dir] += num
    elif dir == 'S':
        pos['N'] -= num
    else:
        pos['E'] -= num

def pt1(input):
    turns = ['N', 'E', 'S', 'W']
    facing = 'E'
    pos = {'E' : 0, 'N' : 0}
    for line in input:
        cmd = line[0]
        num = int(line[1:])
        if cmd in ['N', 'S', 'E', 'W']:
            move(pos, cmd, num)
        elif cmd == 'F':
            move(pos, facing, num)
        elif cmd in ['R', 'L']:
            num = num // 90
            if cmd == 'R':
                facing = turns[(turns.index(facing) + num) % 4]
            else:
                facing = turns[(turns.index(facing) - num) % 4]
    return abs(pos['N']) + abs(pos['E'])

def pt2(input):
    way_pos = {'N' : 1, 'E' : 10}    
    ship_pos = {'N' : 0, 'E' : 0}
    for line in input:
        cmd = line[0]
        num = int(line[1:])
        if cmd in ['N', 'S', 'E', 'W']:
            move(way_pos, cmd, num)
        elif cmd == 'F':
            move(ship_pos, 'N', way_pos['N'] * num)
            move(ship_pos, 'E', way_pos['E'] * num)
        elif cmd in ['R', 'L']:
            x = way_pos['E']
            y = way_pos['N']
            if cmd == 'R':
                num = abs(360 - num)
            if num == 90:
                way_pos['E'], way_pos['N'] = -y, x
            elif num == 180:
                way_pos['E'], way_pos['N'] = -x, -y
            elif num == 270:
                way_pos['E'], way_pos['N'] = y, -x
    return abs(ship_pos['N']) + abs(ship_pos['E'])

with open(sys.argv[1]) as f:
    input = [line.strip() for line in f]
    print(pt1(input))
    print(pt2(input))







