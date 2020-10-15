#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""day21.py: Advent of Code 2019 --- Day 21: Springdroid Adventure ---
   https://adventofcode.com/2019/day/21
"""

__version__ = "1.0"
__maintainer__ = "Jiří Řepík"
__email__ = "jiri.repik@gmail.com"
__status__ = "Submited"

import advent
from utils import *
from lib.intcode import intcode_oneshot

def download_input_data():
    global fin
    advent.setup(2019, 21, dry_run=False)
    fin = advent.get_input()


def part01():
    global program 
    springscript = """\
    NOT A J
    NOT J J
    AND B J
    AND C J
    NOT J J
    AND D J
    WALK
    """
    program = list(map(int, fin.read().split(',')))
    inp = list(map(ord, springscript))
    for value in intcode_oneshot(program, inp):
	    continue

    assert value == 19353619
    advent.submit_answer(2, value)

def part02():
    springscript = """\
    NOT C J
    AND H J
    NOT B T
    OR T J
    NOT A T
    OR T J
    AND D J
    RUN
    """

    inp = list(map(ord, springscript))
    for value in intcode_oneshot(program, inp):
	    continue

    assert value == 1142785329
    advent.submit_answer(2, value)

if __name__ == "__main__":
    download_input_data()
    timer_start()
    part01()
    part02()
