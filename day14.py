#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""day14.py: Advent of Code 2019 --- Day 14: Space Stoichiometry ---
   https://adventofcode.com/2019/day/14
"""

__version__ = "1.0"
__maintainer__ = "Jiří Řepík"
__email__ = "jiri.repik@gmail.com"
__status__ = "Submited"

import advent
from utils import *
from copy import deepcopy

def download_input_data():
    global fin
    advent.setup(2019, 14)
    fin = advent.get_input()

def solve(wanted_fuel):
    want = defaultdict(int)
    want['FUEL'] = wanted_fuel

    _left = deepcopy(left)
    _left['FUEL'] = 0

    while 1:
        goal = min(_left, key=_left.get)
        assert _left[goal] == 0
        del _left[goal]

        if goal == 'ORE':
            ans = want[goal]
            break

        wanted_qty = want[goal]
        recipe_qty = produced[goal]
        multiplier = wanted_qty // recipe_qty

        if wanted_qty % recipe_qty != 0:
            multiplier += 1

        for req, nreq in needed[goal].items():
            want[req] += nreq * multiplier
            _left[req] -= 1

    return ans

def part01():
    global left
    global produced
    global needed

    lines = get_lines(fin)

    produced = {}
    needed = {}
    left = defaultdict(int)

    for l in lines:
        a, b = l.split(' => ')
        aa = a.split(', ')
    
        b = b.split()
        b_num, b_name = int(b[0]), b[1]

        produced[b_name] = b_num
        needed[b_name] = {}

        for el in aa:
            x = el.split()
            a_num, a_name = int(x[0]), x[1]
    
            needed[b_name][a_name] = a_num
            left[a_name] += 1

    ans = solve(1)
    advent.submit_answer(1, ans)

def part02():
    n = 1000000000000
    s = solve(n)
    advent.submit_answer(1, s)

if __name__ == "__main__":
    download_input_data()
    timer_start()
    part01()
    part02()
