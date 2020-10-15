#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""day12.py: Advent of Code 2019 --- Day 12: The N-Body Problem ---
   https://adventofcode.com/2019/day/12
"""

__version__ = "1.0"
__maintainer__ = "Jiří Řepík"
__email__ = "jiri.repik@gmail.com"
__status__ = "Submited"

import advent
from utils import *
import re
from math import gcd
from functools import reduce
from collections import namedtuple
from itertools import combinations, count

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def download_input_data():
    global fin 
    advent.setup(2019, 12, dry_run=False)
    fin = advent.get_input()

def part01():
    global step
    global moons
    exp = re.compile(r'-?\d+')
    initial_positions = [list(map(int, exp.findall(line))) for line in fin]

    Moon = namedtuple('Moon', ['pos', 'vel'])
    moons = [Moon(pos.copy(), [0, 0, 0]) for pos in initial_positions]

    for step in range(1000):
        for moon1, moon2 in combinations(moons, 2):
            for dim in range(3):
                if moon2.pos[dim] > moon1.pos[dim]:
                    moon1.vel[dim] += 1
                    moon2.vel[dim] -= 1
                elif moon2.pos[dim] < moon1.pos[dim]:
                    moon1.vel[dim] -= 1
                    moon2.vel[dim] += 1

        for moon in moons:
            for dim in range(3):
                moon.pos[dim] += moon.vel[dim]

    potential = (sum(map(abs, m.pos)) for m in moons)
    kinetic   = (sum(map(abs, m.vel)) for m in moons)
    total     = sum(p * k for p, k in zip(potential, kinetic))

    assert total == 8742
    advent.submit_answer(1, total)

def part02():
    periods = []
    start = step + 1

    for dim in range(3):
        for period in count(start):
            if all(m.vel[dim] == 0 for m in moons):
                break

            for moon1, moon2 in combinations(moons, 2):
                if moon2.pos[dim] > moon1.pos[dim]:
                    moon1.vel[dim] += 1
                    moon2.vel[dim] -= 1
                elif moon2.pos[dim] < moon1.pos[dim]:
                    moon1.vel[dim] -= 1
                    moon2.vel[dim] += 1
    
            for moon in moons:
                moon.pos[dim] += moon.vel[dim]

        periods.append(period)

    total_steps = 2 * reduce(lcm, periods, 1)

    assert total_steps == 325433763467176
    advent.submit_answer(2, total_steps)

if __name__ == "__main__":
    download_input_data()
    timer_start()
    part01()
    part02()
