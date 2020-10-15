#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""day04.py: Advent of Code 2019 --- Day 4: Secure Container ---
   https://adventofcode.com/2019/day/4
"""

__version__ = "1.0"
__maintainer__ = "Jiří Řepík"
__email__ = "jiri.repik@gmail.com"
__status__ = "Submited"

import advent
from utils import *
from itertools import islice

def download_input_data():
    global fin
    advent.setup(2019, 4, dry_run=False)
    fin = advent.get_input()


def part0102():
    global fin
    lo, hi = map(int, fin.read().split('-'))
    n_valid1 = 0
    n_valid2 = 0

    for pwd in range(lo, hi + 1):
        digits = str(pwd)
        pairs = tuple(zip(digits, digits[1:]))

        if all(a <= b for a, b in pairs) and any(a == b for a, b in pairs):
            n_valid1 += 1
    
            digits = 'x' + digits + 'x'
            quadruplets = zip(digits, digits[1:], digits[2:], digits[3:])

            if any(a != b and b == c and c != d for a, b, c, d in quadruplets):
                n_valid2 += 1


    assert n_valid1 == 931
    advent.submit_answer(1, n_valid1)

    assert n_valid2 == 609
    advent.submit_answer(2, n_valid2)

if __name__ == "__main__":
    download_input_data()
    timer_start()
    part0102()
