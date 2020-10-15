#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""day01.py: Advent of Code 2019 --- Day 1: The Tyranny of the Rocket Equation ---
   https://adventofcode.com/2019/day/1
"""

__version__ = "1.0"
__maintainer__ = "Jiří Řepík"
__email__ = "jiri.repik@gmail.com"
__status__ = "Submited"

import advent
from utils import *

def download_input_data():
    global fin
    global nums    
    advent.setup(2019, 1, dry_run=False)
    fin = advent.get_input()
    nums = map(int, fin.readlines())
    

def part01():
    global fin 
    global nums
    global total
    nums = tuple(map(lambda n: n // 3 - 2, nums))
    total = sum(nums)

    assert total == 3363929
    advent.submit_answer(1, total)

def part02():
    global fin 
    global nums
    global total
    for n in nums:
        while n > 0:
            n = max(n // 3 - 2, 0)
            total += n
    assert total == 5043026
    advent.submit_answer(2, total)

if __name__ == "__main__":
    download_input_data()
    timer_start()
    part01()
    part02()
