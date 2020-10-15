#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Advent of Code 2019 --- execute all days ---
"""

__version__ = "1.0"
__maintainer__ = "Jiří Řepík"
__email__ = "jiri.repik@gmail.com"
__status__ = "Submited"


from utils import *
import os

timer_start()
for day in range(1,25):
	os.system(f"python3 day{str(day).zfill(2)}.py")


