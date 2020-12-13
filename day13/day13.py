#!/usr/bin/env python
import sys

with open(sys.argv[1]) as f:
    depart = int(f.readline().strip())
    busses = f.readline().strip().split(',')
#Part 1
tups = [(int(t), int(t) - depart % int(t)) for t in busses if t != 'x']
bus = min(tups, key=lambda x:x[1])
print(bus[0] * bus[1])

#Part2
#Tuple with bus id and offset
bus_tuples = [(int(bus), i) for i, bus in enumerate(busses) if bus != "x"]
step = int(bus_tuples[0][0])
i = 0
solved = 0
while solved < len(bus_tuples) - 1:
    i += step
    for num, bus in enumerate(bus_tuples):
        if (i + bus[1]) % bus[0] != 0:
            break
        if solved < num:
            solved += 1
            step = step * bus[0]
print(i)




    




