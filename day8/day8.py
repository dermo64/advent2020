#!/usr/bin/env python
import sys
def run_program(program):
    pc, acc = 0, 0
    visited = {}
    while pc < len(program):
        next = 1
        if program[pc][0] == 'acc':
            acc += int(program[pc][1])
        elif program[pc][0] == 'jmp':
            next = int(program[pc][1])
        if pc + next in visited:
            raise ValueError(f"Infinte Loop: acc:{acc}")
        visited[pc] = 1
        pc += next
    return acc
    
with open(sys.argv[1]) as f:
    program = [line.strip().split() for line in f]
    #Part 1
    try:    
        print(run_program(program))
    except Exception as e:
        print(f"Had an infinite loop {str(e)}")
    #Part 2
    for index, line in enumerate(program):
        if line[0] == 'acc':
            continue
        old_op = line[0]
        if line[0] == 'nop':
            program[index][0] = 'jmp'
        elif line[0] == 'jmp':
            program[index][0] = 'nop'
        try:    
            print(run_program(program))
            break
        except:
            program[index][0] = old_op
        




