#!/usr/bin/env python
import re
import sys

def can_contain(bags, parent, bag):
    for i in bags[parent]:
        if i[1] == bag:
            return True
        if can_contain(bags, i[1], bag):
            return True
    return False

def num_bags(bags, parent):
    num = 1
    for i in bags[parent]:
        num += (int(i[0]) * num_bags(bags, i[1]))
    return num

with open(sys.argv[1]) as f:
    bag_dict = {}
    for line in f:
        m = re.match(r'^(\w+\s+\w+)\sbags contain (.*)', line)
        parent = m.group(1)
        children = m.group(2).split(',')
        bag_dict[parent] = set()
        for i in children:
            m = re.match(r'(\d+) (\w+ \w+) bag', i.strip())
            if m is not None: 
                bag_dict[parent].add((m.group(1), m.group(2)))        

print([can_contain(bag_dict, bag, 'shiny gold') for bag in bag_dict].count(True))
print(num_bags(bag_dict, 'shiny gold') - 1)