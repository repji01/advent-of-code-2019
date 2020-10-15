#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""day19.py: Advent of Code 2019 --- Day 19: Tractor Beam ---
   https://adventofcode.com/2019/day/19
"""

__version__ = "1.0"
__maintainer__ = "Jiří Řepík"
__email__ = "jiri.repik@gmail.com"
__status__ = "Submited"

import advent
from utils import *
from itertools import product, count
from lib.intcode import intcode_oneshot

def run(inp):
    return next(intcode_oneshot(program, inp))

def get_width(x, target):
    for top in count(0):
        if run((x, top)) == 1:
            break

    if run((x, top + target)) == 0:
        return 0, 0

    for bottom in count(top + target + 1):
        if run((x, bottom)) == 0:
            break

    y = bottom - target

    for width in count(1):
        if run((x + width, y)) == 0:
            break

    return width, y

def bin_search(lo, hi, target):
    best = None

    while hi - lo > 1:
        x = (lo + hi) // 2
        
        width, y = get_width(x, target)
        print('bin' + str(best))
        if width > target:
            hi = x
            best = (x, y)
        elif width < target:
            lo = x

    return best

def download_input_data():
    global fin
    advent.setup(2019, 19, dry_run=False)
    fin = advent.get_input()

def part01():
    global program
    program = list(map(int, fin.read().split(',')))
    total = sum(map(run, product(range(50), range(50))))

    assert total == 169
    advent.submit_answer(1, total)

def part02():
    TARGET = 100
    bestx, besty = (712, 1155) #bin_search(10, 9999, TARGET)

    for x in range(bestx, bestx - 10, -1):
        width, y = get_width(x, TARGET)
        if width >= TARGET:
            bestx, besty = x, y

    answer = bestx * 10000 + besty
    assert answer == 7001134
    advent.submit_answer(2, answer)

if __name__ == "__main__":
    download_input_data()
    timer_start()
    part01()
    part02()
