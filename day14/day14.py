#!/usr/bin/env python
import sys
import re

with open(sys.argv[1]) as f:
    input = [line for line in f]
    and_mask = 0
    or_mask = 0
    mem = {}
    mem2 = {}
    for line in input:
        m = re.match(r'^mask = ([10X]+)', line)
        if m != None:
            mask = m.group(1)
            and_mask = int(mask.replace('X','1'), 2)
            or_mask = int(mask.replace('X','0'), 2)
        else:
            #part1
            m = re.match(r'^mem\[(\d+)\] = (\d+)', line)
            location = int(m.group(1))
            val = int(m.group(2))
            mem[location] = (val & and_mask) | or_mask

            #part2
      #      print(f'{location:>036b}')
       #     print(f'{or_mask:>036b}')
            location = location | or_mask

            bits = mask.count('X')
            for i in range(2**bits):
                loc = list(f'{location:>036b}')
                floats = f'{i:>b}'.rjust(bits, "0")
              #  print(floats)
                for j, char in enumerate(mask):
                    if char == 'X':
                        loc[j] = floats[0]
                        floats = floats[1:]
                mem2[(int(''.join(loc),2))] = val

    print(sum(mem.values()))

    print(sum(mem2.values()))



    




