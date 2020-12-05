#!/usr/bin/env python

import sys
import string

def seatid_to_num(seat):
    return int(''.join(['1' if digit == 'B' or digit == 'R' else '0' for digit in seat]), 2)

def get_seatid(seat):
    row = (seat &  ~7) >> 3
    col = seat & 7
    return (row * 8) + col

with open(sys.argv[1]) as f:
    input = [seatid_to_num(line.strip()) for line in f.readlines()]

    #Part 1
    seat_ids = [get_seatid(seat_id) for seat_id in input]
    print(max(seat_ids))

    #Part 2
    seat_nums = [seat_id for seat_id in input]
    print(set(range(min(seat_nums), max(seat_nums) + 1)) - set(seat_nums))
