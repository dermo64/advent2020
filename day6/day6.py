#!/usr/bin/env python

import sys

with open(sys.argv[1]) as f:
    answers = {}
    total_pt1, total_pt2, count = 0, 0, 0
    
    for line in f:
        if line.strip() == "":
            for k, v in answers.items():
                if v == count:
                    total_pt2 += 1
            total_pt1 += len(answers)
            answers = {}
            count = 0
        else:
            for char in line.strip():
                if char in answers:
                    answers[char] += 1
                else:
                    answers[char] = 1
            count += 1

    for k,v in answers.items():
        if v == count:
            total_pt2 += 1              
    total_pt1 += len(answers)

    print(total_pt1)
    print(total_pt2)
