#!/usr/bin/env python
import sys

def part1(data):
    jolt_deltas = list()
    joltage = 0
    for i in data:
        jolt_deltas.append(i-joltage)
        joltage = i
    part1 = jolt_deltas.count(1) * (jolt_deltas.count(3))
    return part1

def num_configs(joltage, adapters, cache):
    if joltage in cache:
        return cache[joltage]
    if len(adapters) == 1:
        return 1
    num = 0
    if adapters[0] - joltage < 4:
        num += num_configs(adapters[0], adapters[1:], cache)
    if len(adapters) > 2 and adapters[1] - joltage < 4:
        num += num_configs(adapters[1], adapters[2:], cache)
    if len(adapters) > 3 and adapters[2] - joltage < 4:
        num += num_configs(adapters[2], adapters[3:], cache)
    cache[joltage] = num
    return num
         
with open(sys.argv[1]) as f:
    data = sorted([int(line.strip()) for line in f])
    data.append(3+max(data))
    print(part1(data))
    print(num_configs(0, data, {}))




