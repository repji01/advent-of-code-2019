#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""day09.py: Advent of Code 2019 --- Day 9: Sensor Boost ---
   https://adventofcode.com/2019/day/9
"""

__version__ = "1.0"
__maintainer__ = "Jiří Řepík"
__email__ = "jiri.repik@gmail.com"
__status__ = "Submited"

import advent
from utils import *
from lib.intcode import IntcodeVM

def download_input_data():
    global fin
    advent.setup(2019, 9, dry_run=False)
    fin = advent.get_input()

def part01():
    global vm
    program = list(map(int, fin.read().split(',')))
    vm = IntcodeVM(program)
    out = vm.run([1])[-1]

    assert out == 2941952859
    advent.submit_answer(1, out)

def part02():
    out = vm.run([2])[-1]

    assert out == 66113
    advent.submit_answer(2, out)

if __name__ == "__main__":
    download_input_data()
    timer_start()
    part01()
    part02()
