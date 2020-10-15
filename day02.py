#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""day02.py: Advent of Code 2019 --- Day 2: 1202 Program Alarm ---
   https://adventofcode.com/2019/day/2
"""

__version__ = "1.0"
__maintainer__ = "Jiří Řepík"
__email__ = "jiri.repik@gmail.com"
__status__ = "Submited"

import advent
from utils import *
from operator import add, mul
from itertools import product


def run(prog, *inputs):
    prog[1:3] = inputs[:]
    pc = 0

    while prog[pc] != 99:
        op = add if prog[pc] == 1 else mul
        a, b, c = prog[pc + 1:pc + 4]
        prog[c] = op(prog[a], prog[b])
        pc += 4

    return prog[0]

def download_input_data():
    global fin
    advent.setup(2019, 2, dry_run=False)
    fin = advent.get_input()
    timer_start()

def part01():
    global fin 
    global nums
    global total
    global program
    program = list(map(int, fin.read().split(',')))
    result = run(program[:], 12, 2)
    assert result == 12490719
    advent.submit_answer(1, result)

def part02():
    for noun, verb in product(range(100), range(100)):
        if run(program[:], noun, verb) == 19690720:
            break
    answer = 100 * noun + verb
    assert answer == 2003
    advent.submit_answer(2, answer)

if __name__ == "__main__":
    download_input_data()
    timer_start()
    part01()
    part02()
