#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""day10.py: Advent of Code 2019 --- Day 10: Monitoring Station ---
   https://adventofcode.com/2019/day/10
"""

__version__ = "1.0"
__maintainer__ = "Jiří Řepík"
__email__ = "jiri.repik@gmail.com"
__status__ = "Submited"

import advent
from utils import *
from math import atan2, gcd, pi as PI

def ray(ax, ay, bx, by):
    dx, dy = bx - ax, by - ay
    div = abs(gcd(dx, dy))
    return dx//div, dy//div

def manhattan(ax, ay, bx, by):
    return abs(bx - ax) + abs(by - ay)

def angle(ax, ay, bx, by):
    rad = atan2(by-ay, bx-ax) + PI
    rad = rad % (2*PI) - PI/2
    return rad if rad >= 0 else 2*PI + rad

def download_input_data():
    global fin    
    advent.setup(2019, 10, dry_run=False)
    fin = advent.get_input()

def part01():
    global max_in_sight
    global asteroids
    global station
    grid = [l.rstrip() for l in fin]
    asteroids = set()

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == '#':
                asteroids.add((x, y))

    station = None
    max_in_sight = 0

    for src in asteroids:
        lines_of_sight = set()

        for a in asteroids:
            if a == src:
                continue

            lines_of_sight.add(ray(*src, *a))

        in_sight = len(lines_of_sight)
        if in_sight > max_in_sight:
            max_in_sight = in_sight
            station = src

    assert max_in_sight == 326
    advent.submit_answer(1, max_in_sight)

def part02():
    closest = {}
    target = 200

    assert max_in_sight >= target

    for a in asteroids:
        if a == station:
            continue

        r = ray(*station, *a)
        m = manhattan(*station, *a)

        if r not in closest or m < closest[r][1]:
            closest[r] = (a, m)

    ordered = sorted(closest.values(), key=lambda am: angle(*station, *am[0]))
    chosen_x, chosen_y = ordered[target - 1][0]
    ans = 100 * chosen_x + chosen_y

    assert ans == 1623
    advent.submit_answer(2, ans)

if __name__ == "__main__":
    download_input_data()
    timer_start()
    part01()
    part02()
