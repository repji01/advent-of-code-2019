#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""day07.py: Advent of Code 2019 --- Day 7: Amplification Circuit ---
   https://adventofcode.com/2019/day/7
"""

__version__ = "1.0"
__maintainer__ = "Jiří Řepík"
__email__ = "jiri.repik@gmail.com"
__status__ = "Submited"

import advent
from utils import *
from itertools import permutations
from lib.intcode import IntcodeVM

def download_input_data():
    global fin
    advent.setup(2019, 7, dry_run=False)
    fin = advent.get_input()

def part01():
    global fin
    global vms
    program = list(map(int, fin.read().split(',')))
    vms = [IntcodeVM(program) for _ in range(5)]
    max_signal = float('-inf')

    for inputs in permutations(range(5), 5):
        out = [0]

        for vm, inp in zip(vms, inputs):
            out = vm.run([inp, *out])

        if out[0] > max_signal:
            max_signal = out[0]

    assert max_signal == 99376
    advent.submit_answer(1, max_signal)

def part02():
    max_signal = float('-inf')

    for inputs in permutations(range(5, 10), 5):
        out = [0]

        for vm, inp in zip(vms, inputs):
            out = vm.run([inp, *out], n_out=1)

        last_signal = out[0]

        while all(vm.running for vm in vms):
            for i, vm in enumerate(vms):
                out = vm.run(out, n_out=1, resume=True)
    
                if not vm.running:
                    break

                if i == 4:
                    last_signal = out[0]

        if last_signal > max_signal:
            max_signal = last_signal

    assert max_signal == 8754464
    advent.submit_answer(2, max_signal)

if __name__ == "__main__":
    download_input_data()
    timer_start()
    part01()
    part02()
