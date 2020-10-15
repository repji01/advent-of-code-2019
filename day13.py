#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""day13.py: Advent of Code 2019 --- Day 13: Care Package ---
   https://adventofcode.com/2019/day/13
"""

__version__ = "1.0"
__maintainer__ = "Jiří Řepík"
__email__ = "jiri.repik@gmail.com"
__status__ = "Submited"

import advent
from utils import *
from lib.intcode import IntcodeVM

EMPTY, WALL, BLOCK, PADDLE, BALL = range(5)

def download_input_data():
    global fin
    advent.setup(2019, 13, dry_run=False)
    fin = advent.get_input()

def part01():
    global vm
    program = list(map(int, fin.read().split(',')))

    vm = IntcodeVM(program)
    out = vm.run()
    blocks = set()

    for i in range(0, len(out), 3):
        x, y, t = out[i:i + 3]
        if t == BLOCK:
            blocks.add((x, y))

    total_blocks = len(blocks)

    assert total_blocks == 301
    advent.submit_answer(1, total_blocks)

def part02():
    vm.orig_code[0] = 2
    vm.reset()

    score    = 0
    paddle_x = 0
    inp      = []

    while True:
        out = vm.run(inp, resume=True, n_out=3)
        if not out:
            break

        x, y, tile = out
        inp = [0]

        if (x, y) == (-1, 0):
            score = tile
            continue

        if tile == PADDLE:
            paddle_x = x
        elif tile == BALL:
            if x > paddle_x:
                inp[0] = 1
            elif x < paddle_x:
                inp[0] = -1

    assert score == 14096
    advent.submit_answer(2, score)

if __name__ == "__main__":
    download_input_data()
    timer_start()
    part01()
    part02()
