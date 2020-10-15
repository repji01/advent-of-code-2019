#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""advent.py: Advent of Code 2019 
   https://adventofcode.com/2019/
"""

__version__ = "1.0"
__maintainer__ = "Jiří Řepík"
__email__ = "jiri.repik@gmail.com"
__status__ = "Submited"


import os
import sys
import re
import time
from importlib.util import find_spec
from datetime import datetime, timedelta

def log(s, *a):
    """Write log message to error output"""
    sys.stderr.write(s.format(*a))
    sys.stderr.flush()

def check_or_die(resp):
    """Check cookie for submiting solution"""
    pls_identify = 'please identify yourself' in resp.text.lower()

    if resp.status_code != 200:
        log('\n[advent] ERROR: response {}, url: {}\n', resp.status_code, resp.url)
        log('[advent] Did you log in and update your session cookie?\n')
        sys.exit(1)
    elif pls_identify:
        log('\n[advent] ERROR: Server returned 200, but is asking for identification.\n')
        log('[advent] Did you log in and update your session cookie?\n')
        sys.exit(1)

def setup(year, day, dry_run=False):
    """Setup day and whether we want to submit the solution"""
    global YEAR
    global DAY
    global DRY_RUN
    global SESSION

    assert year >= 2015
    assert 1 <= day <= 25

    YEAR    = year
    DAY     = day
    DRY_RUN = dry_run

    if REQUESTS and os.path.isfile('secret_session_cookie'):
        with open('secret_session_cookie') as f:
            SESSION = f.read().rstrip()
            s.cookies.set('session', SESSION)

def get_input(fname=None, mode='r'):
    """Get input data for the day"""
    if not os.path.isdir(CACHE_DIR):
        try:
            os.mkdir(CACHE_DIR)
            log("[advent] Created cache directory '{}' since it did not exist.\n", CACHE_DIR)
        except Exception as e:
            log("[advent] ERROR: could not create cache directory '{}'.\n", CACHE_DIR)
            log('[advent] {}\n', str(e))
            sys.exit(1)

    log('[advent] Getting input for year {} day {}... ', YEAR, DAY)

    if fname is None:
        fname = os.path.join(CACHE_DIR, '{}_{:02d}.txt'.format(YEAR, DAY))

    if not os.path.isfile(fname):
        if not REQUESTS:
            log('err!\n')
            log('[advent] ERROR: cannot download input, no requests module installed!\n')
            sys.exit(1)
        elif not SESSION:
            log('err!\n')
            log('[advent] ERROR: cannot download input file without session cookie!\n')
            sys.exit(1)

        log('downloading... ')

        r = s.get(URL.format(YEAR, DAY, 'input'))
        check_or_die(r)

        with open(fname, 'wb') as f:
            f.write(r.content)

        log('done.\n')

    else:
        log('done (from disk).\n')

    return open(fname, mode)

def submit_answer(part, answer):
    """Submit the solution"""
    if DRY_RUN:
        print('Part {}: {}'.format(part, answer))
    elif not REQUESTS:
        log('[advent] Cannot upload answer, no requests module installed!\n')
        print('Part {}: {}'.format(part, answer))
    else:
        log('[advent] Submitting day {} part {} answer: {}\n', DAY, part, answer)

        r = s.post(URL.format(YEAR, DAY, 'answer'), data={'level': part, 'answer': answer})
        check_or_die(r)

        t = r.text.lower()

        if 'did you already complete it' in t:
            log('[advent] Already completed!\n')
            return True

        if "that's the right answer" in t:
            log('[advent] Right answer!\n')
            return True

        log('[advent] Wrong answer :(\n')
        return False

URL       = 'https://adventofcode.com/{:d}/day/{:d}/{:s}'
SESSION   = ''
CACHE_DIR = 'inputs'
YEAR      = -1
DAY       = -1
DRY_RUN   = False
REQUESTS  = find_spec('requests')

if REQUESTS:
    import requests
    s = requests.Session()

