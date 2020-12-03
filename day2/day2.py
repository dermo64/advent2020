#!/usr/bin/env python
import sys
import re

count_pt1, count_pt2 = 0, 0
with open(sys.argv[1]) as f:
    for line in f:
        m = re.match(r'(\d+)-(\d+) ([a-z]): ([a-z]+)', line)
        num1, num2, letter, password = int(m.group(1)), int(m.group(2)), m.group(3), m.group(4)
        occurences = password.count(letter)
        if occurences >= num1 and occurences <= num2:
            count_pt1 += 1
        if (password[num1-1] == letter) ^ (password[num2-1] == letter):
            count_pt2 += 1
        
print(count_pt1)
print(count_pt2)

    
