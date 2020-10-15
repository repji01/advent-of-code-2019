#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""day03.py: Advent of Code 2019 --- Day 3: Crossed Wires ---
   https://adventofcode.com/2019/day/3
"""

__version__ = "1.0"
__maintainer__ = "Jiří Řepík"
__email__ = "jiri.repik@gmail.com"
__status__ = "Submited"

import advent
from utils import *

MOVE_DX = {'U': 0, 'D':  0, 'R': 1, 'L': -1}
MOVE_DY = {'U': 1, 'D': -1, 'R': 0, 'L':  0}

def make_move(s):
    return s[0], int(s[1:])

def get_visited_and_steps(moves):
    p = (0, 0)
    cur_steps = 0
    visited = set()
    steps = {}

    for d, n in moves:
        for _ in range(n):
            p = (p[0] + MOVE_DX[d], p[1] + MOVE_DY[d])
            visited.add(p)
            cur_steps += 1

            if p not in steps:
                steps[p] = cur_steps

    return visited, steps

def manhattan(p):
    return abs(p[0]) + abs(p[1])

def download_input_data():
    global lines    
    advent.setup(2019, 3, dry_run=False)
    lines = advent.get_input().readlines()

def part01():
    global intersections
    global all_steps
    global lines    
    all_visited = []
    all_steps = []

    for l in lines:
        visited, steps = get_visited_and_steps(map(make_move, l.split(',')))
        all_visited.append(visited)
        all_steps.append(steps)

    intersections = set.intersection(*all_visited)
    min_distance = min(map(manhattan, intersections))

    assert min_distance == 352
    advent.submit_answer(1, min_distance)

def part02():
    global intersections
    global all_steps
    shortest_path = min(sum(l[p] for l in all_steps) for p in intersections)
    assert shortest_path == 43848
    advent.submit_answer(2, shortest_path)

if __name__ == "__main__":
    download_input_data()
    timer_start()
    part01()
    part02()
