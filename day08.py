#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""day08.py: Advent of Code 2019 --- Day 8: Space Image Format ---
   https://adventofcode.com/2019/day/8
"""

__version__ = "1.0"
__maintainer__ = "Jiří Řepík"
__email__ = "jiri.repik@gmail.com"
__status__ = "Submited"

import advent
from utils import *

WIDTH, HEIGHT = 25, 6
SIZE = WIDTH * HEIGHT

def download_input_data():
    global fin
    advent.setup(2019, 8, dry_run=False)
    fin = advent.get_input()

def part01():
    global fin
    global layers
    chars = fin.readline().strip()
    layers = [chars[i:i + SIZE] for i in range(0, len(chars), SIZE)]

    best = min(layers, key=lambda l: l.count('0'))
    checksum = best.count('1') * best.count('2')

    assert checksum == 1206
    advent.submit_answer(1, checksum)

def part02():

    image = ['2'] * SIZE

    for i in range(SIZE):
    	for l in layers:
    		if l[i] != '2':
    			image[i] = l[i]
    			break

    conv = {'0': ' ', '1': '#'}
    decoded = ''

    for i in range(0, SIZE, WIDTH):
    	decoded += ''.join(map(conv.get, image[i:i + WIDTH])) + '\n'
    print(decoded)
    assert (decoded ==
    	'####   ## ###   ##  ###  \n'
    	'#       # #  # #  # #  # \n'
    	'###     # #  # #    #  # \n'
    	'#       # ###  # ## ###  \n'
    	'#    #  # # #  #  # #    \n'
    	'####  ##  #  #  ### #    \n'
    )
    advent.submit_answer(2, 'EJRGP')

if __name__ == "__main__":
    download_input_data()
    timer_start()
    part01()
    part02()

