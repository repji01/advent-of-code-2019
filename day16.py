#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""day16.py: Advent of Code 2019 --- Day 16: Flawed Frequency Transmission ---
   https://adventofcode.com/2019/day/16
"""

__version__ = "1.0"
__maintainer__ = "Jiří Řepík"
__email__ = "jiri.repik@gmail.com"
__status__ = "Submited"

import advent
from utils import *

def download_input_data():
    global fin
    advent.setup(2019, 16, dry_run=False)
    fin = advent.get_input()

def  part01():
    global original_str
    global original
    original_str = fin.read().strip()
    original = list(map(int, original_str))
    digits = original[:]
    length = len(digits)

    for _ in range(100):
        old = digits[:]

        for i in range(length//2 + 1):
            j = i
            step = i + 1
            cur = 0
    
            while j < length:
                cur += sum(old[j:j + step])
                j += 2 * step
    
                cur -= sum(old[j:j + step])
                j += 2 * step
    
            digits[i] = abs(cur) % 10

        cusum = 0
        for i in range(length - 1, length//2, -1):
            cusum += digits[i]
            digits[i] = cusum % 10

    answer = ''.join(map(str, digits[:8]))

    assert answer == '50053207'
    advent.submit_answer(1, answer)



def part02_helper(digits, skip):
    digits = (original*10000)[skip:]
    length = len(digits)

    assert skip > length//2

    for _ in range(100):
        cusum = 0
        for i in range(length - 1, -1, -1):
            cusum += digits[i]
            digits[i] = cusum % 10

    return ''.join(map(str, digits[:8]))

def part02():
    skip = int(''.join(original_str[:7]))
    answer = part02_helper(original, skip)

    assert answer == '32749588'
    advent.submit_answer(2, answer)

if __name__ == "__main__":
    download_input_data()
    timer_start()
    part01()
    part02()
