#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""day18.py: Advent of Code 2019 --- Day 18: Many-Worlds Interpretation ---
   https://adventofcode.com/2019/day/18
"""

__version__ = "1.0"
__maintainer__ = "Jiří Řepík"
__email__ = "jiri.repik@gmail.com"
__status__ = "Submited"

import advent
from utils import *
from string import ascii_lowercase as lowercase, ascii_uppercase as uppercase

def download_input_data():
    global fin
    advent.setup(2019, 18, dry_run=False)
    fin = advent.get_input()

def neigh4(r, c):
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        rr, cc = (r + dr, c + dc)
        if 0 <= rr < len(grid) and 0 <= cc < len(grid[rr]):
            if grid[rr][cc] != '#':
                yield (rr, cc)

@lru_cache(maxsize=2**30)
def reachable_keys(src, mykeys):
    # part 1
    queue = deque([(0, src)])
    visited = set()
    foundkeys = {}

    while queue:
        dist, node = queue.popleft()

        if node not in visited:
            visited.add(node)

            if node in keys:
                k = keys[node]

                if k not in mykeys and (k not in foundkeys or foundkeys[k] > dist):
                    foundkeys[k] = dist
                    continue

            if node in doors and not doors[node] in mykeys:
                continue

            for neighbor in filter(lambda n: n not in visited, G[node]):
                new_dist = dist + 1
                queue.append((new_dist, neighbor))

    return foundkeys

@lru_cache(maxsize=2**30)
def search(pos, mykeys=frozenset()):
    # part 1
    keyz = reachable_keys(pos, mykeys)
    if not keyz:
        if len(mykeys) == len(keys)//2:
            return 0
        else:
            return float('inf')

    best = float('inf')

    for k, d in keyz.items():
        keypos = keys[k]
        dist = d + search(keypos, mykeys | {k})

        if dist < best:
            best = dist

    return best

@lru_cache(maxsize=2**30)
def reachable_keys2(srcs, mykeys):
    # part2
    queue = deque()
    visited = set()
    foundkeys = {}

    for src in srcs:
        queue.append((0, src, src))

    while queue:
        dist, node, owner = queue.popleft()

        if node not in visited:
            visited.add(node)

            if node in keys:
                k = keys[node]

                if k not in mykeys and (k not in foundkeys or foundkeys[k] > dist):
                    foundkeys[k] = (owner, dist)
                    continue

            if node in doors and not doors[node] in mykeys:
                continue

            for neighbor in filter(lambda n: n not in visited, G[node]):
                queue.append((dist + 1, neighbor, owner))

    return foundkeys

@lru_cache(maxsize=2**30)
def search2(bots, mykeys=frozenset()):
    # part 2
    keyz = reachable_keys2(bots, mykeys)
    if not keyz:
        if len(mykeys) == len(keys)//2:
            return 0
        else:
            return float('inf')

    best = float('inf')

    for k, (owner, d) in keyz.items():
        newbots = []

        for b in bots:
            if b == owner:
                newbots.append(keys[k])
            else:
                newbots.append(b)

        newbots = tuple(newbots)
        dist = d + search2(newbots, mykeys | {k})

        if dist < best:
            best = dist

    return best

def part01():
    global grid
    global keys
    global doors
    global G
    global mypos

    grid = get_char_matrix(fin)

    G = {}
    keys = {}
    doors = {}
    mypos = None

    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            pos = (r, c)
            if cell != '#':
                if pos not in G:
                    G[pos] = set()
    
                for n in neigh4(*pos):
                    G[pos].add(n)

                if cell in lowercase:
                    keys[cell] = pos
                    keys[pos] = cell
                elif cell in uppercase:
                    doors[cell.lower()] = pos
                    doors[pos] = cell.lower()
                elif cell == '@':
                    mypos = pos


    ans = search(mypos)
    advent.submit_answer(1, ans)

def part02():
    del G[mypos]

    for n in neigh4(*mypos):
        del G[n]

        for nn in neigh4(*n):
            if nn in G:
                G[nn].remove(n)

    r, c = mypos
    bots = (
        (r + 1, c + 1),
        (r + 1, c - 1),
        (r - 1, c + 1),
        (r - 1, c - 1),
    )

    ans2 = search2(bots)

    advent.submit_answer(2, ans2)

if __name__ == "__main__":
    download_input_data()
    timer_start()
    part01()
    part02()
