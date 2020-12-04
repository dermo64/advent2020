#!/usr/bin/env python

import sys
import string

def is_valid_pt1(passport):
    fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for field in fields:
        if field not in passport:
            return False
    return True  

def is_valid_pt2(passport):
    eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    byr, iyr, eyr, hgt = passport['byr'], passport['iyr'], passport['eyr'], passport['hgt']
    hcl, ecl, pid = passport['hcl'], passport['ecl'], passport['pid']

    if len(byr) != 4 or not byr.isdigit() or int(byr) < 1920 or int(byr) > 2002:
        return False
    elif len(iyr) != 4 or not iyr.isdigit() or int(iyr) < 2010 or int(iyr) > 2020:
        return False
    elif len(eyr) != 4 or not eyr.isdigit() or int(eyr) < 2020 or int(eyr) > 2030:
        return False
    elif (hgt[-2:] not in ['cm', 'in'] 
        or (hgt[-2:] == 'cm' and (int(hgt[:-2]) < 150 or int(hgt[:-2]) > 193))
        or (hgt[-2:] == 'in' and (int(hgt[:-2]) < 59 or int(hgt[:-2]) > 76))):
        return False
    elif (len(hcl) != 7 or hcl[0] != '#' 
        or not all(x.isdigit() or x in string.ascii_lowercase[0:6] for x in hcl[1:])):
        return False
    elif ecl not in eye_colors:
        return False
    elif len(pid) != 9 or not pid.isdigit():
        return False
    return True  

count, count2 = 0, 0
with open(sys.argv[1]) as f:
    input = f.readlines()
    passport = {}
    for line in input:
        if line.strip() == "":
            if is_valid_pt1(passport):
                count += 1
                if is_valid_pt2(passport):
                    count2 += 1
            passport = {}
        else:
            fields = line.split()
            for field in fields:
                delim = field.index(':')
                passport[field[:delim]] = field[delim + 1:]
    if is_valid_pt1(passport):
        count += 1
        if is_valid_pt2(passport):
                count2 += 1    
print(count)
print(count2)