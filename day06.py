#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""day06.py: Advent of Code 2019 --- Day 6: Universal Orbit Map ---
   https://adventofcode.com/2019/day/6
"""

__version__ = "1.0"
__maintainer__ = "Jiří Řepík"
__email__ = "jiri.repik@gmail.com"
__status__ = "Submited"

import advent
from utils import *
import heapq
from collections import defaultdict

def count_orbits(planet):
    total = 0
    while planet in T:
        total += 1
        planet = T[planet]

    return total

def dijkstra(G, src, dst):
    queue = [(0, src)]
    visited = set()
    distance = defaultdict(lambda: float('inf'))
    distance[src] = 0

    while queue:
        dist, planet = heapq.heappop(queue)

        if planet == dst:
            return dist

        if planet not in visited:
            visited.add(planet)

            for neighbor in filter(lambda p: p not in visited, G[planet]):
                new_dist = dist + 1

                if new_dist < distance[neighbor]:
                    distance[neighbor] = new_dist
                    heapq.heappush(queue, (new_dist, neighbor))

    return float('inf')

def download_input_data():
    global fin
    advent.setup(2019, 6, dry_run=False)
    fin = advent.get_input()

def part01():
    global fin
    global orbits
    global T
    orbits = tuple(map(lambda l: l.strip().split(')'), fin.readlines()))

    T = {child: parent for parent, child in orbits}
    n_orbits = sum(map(count_orbits, T))

    assert n_orbits == 223251
    advent.submit_answer(1, n_orbits)

def part02():
    G = defaultdict(set)
    for a, b in orbits:
        G[a].add(b)
        G[b].add(a)

    min_transfers = dijkstra(G, T['YOU'], T['SAN'])

    assert min_transfers == 430
    advent.submit_answer(2, min_transfers)


if __name__ == "__main__":
    download_input_data()
    timer_start()
    part01()
    part02()
