#!/usr/bin/env python3

import advent
from utils import *
from copy import deepcopy
from itertools import product


def neighbors4(grid, r, c):
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nr, nc = r + dr, c + dc

        if 0 <= nr < ROWS and 0 <= nc < COLS:
            yield nr, nc

def neighbors4_alive(grid, r, c):
    return sum(grid[nr][nc] for nr, nc in neighbors4(grid, r, c))

def evolve(grid, r, c):
    alive = neighbors4_alive(grid, r, c)

    if grid[r][c] == BUG:
        if alive == 1:
            return BUG
        return EMPTY

    if alive == 1 or alive == 2:
        return BUG
    return EMPTY

def nextgen(grid):
    new_grid = [[EMPTY] * COLS for _ in range(ROWS)]

    for r, c in product(range(ROWS), range(COLS)):
        new_grid[r][c] = evolve(grid, r, c)

    return new_grid

def recursive_evolve(grid, grid_outer, grid_inner, r, c):
    alive = 0

    if grid_outer is not None:
        if c == 0 and grid_outer[CENTER_ROW][CENTER_COL - 1]: # left
            alive += 1
        if r == 0 and grid_outer[CENTER_ROW - 1][CENTER_COL]: # up
            alive += 1
        if c == MAXCOL and grid_outer[CENTER_ROW][CENTER_COL + 1]: # right
            alive += 1
        if r == MAXROW and grid_outer[CENTER_ROW + 1][CENTER_COL]: # down
            alive += 1

    if grid_inner is not None:
        if (r, c) == (CENTER_ROW, CENTER_COL - 1): # left
            alive += sum(grid_inner[i][0] for i in range(ROWS))
        elif (r, c) == (CENTER_ROW - 1, CENTER_COL): # up
            alive += sum(grid_inner[0][i] for i in range(COLS))
        elif (r, c) == (CENTER_ROW, CENTER_COL + 1): # right
            alive += sum(grid_inner[i][MAXCOL] for i in range(ROWS))
        elif (r, c) == (CENTER_ROW + 1, CENTER_COL): # down
            alive += sum(grid_inner[MAXROW][i] for i in range(COLS))

    alive += neighbors4_alive(grid, r, c)

    if grid[r][c] == BUG:
        if alive == 1:
            return BUG
        return EMPTY

    if alive == 1 or alive == 2:
        return BUG
    return EMPTY

def recursive_nextgen(grids, depth):
    if depth in grids:
        grid = grids[depth]
    else:
        grid = [[EMPTY] * COLS for _ in range(ROWS)]

    new_grid = [[EMPTY] * COLS for _ in range(ROWS)]
    grid_outer = grids.get(depth + 1)
    grid_inner = grids.get(depth - 1)

    for r, c in product(range(ROWS), range(COLS)):
        if (r, c) == (CENTER_ROW, CENTER_COL):
            continue

        new_grid[r][c] = recursive_evolve(grid, grid_outer, grid_inner, r, c)

    return new_grid

def recursive_nextgen(curgrid, rgrid, depth):
	grid = deepcopy(curgrid)

	for r in range(N):
		for c in range(N):
			if (r, c) == (2, 2):
				continue

			cell = recursive_cell(curgrid, rgrid, depth, r, c)
			grid[r][c] = cell

	return grid

def recursive_cell(curgrid, rgrid, depth, r, c):
	alive = 0

	if depth + 1 in rgrid:
		grid_below = rgrid[depth + 1]

		if (r, c) == (2, 1): # left
			alive += sum(grid_below[i][0] == '#' for i in range(N))
			# alive += sum(curgrid[i][j] == '#' for i, j in ((1,1), (2,0), (3,1)))
		elif (r, c) == (1, 2): # up
			alive += sum(grid_below[0][i] == '#' for i in range(N))
			# alive += sum(curgrid[i][j] == '#' for i, j in ((1,1), (0,2), (1,3)))
		elif (r, c) == (2, 3): # right
			alive += sum(grid_below[i][MAX] == '#' for i in range(N))
			# alive += sum(curgrid[i][j] == '#' for i, j in ((1,3), (2,4), (3,3)))
		elif (r, c) == (3, 2): # down
			alive += sum(grid_below[MAX][i] == '#' for i in range(N))
			# alive += sum(curgrid[i][j] == '#' for i, j in ((3,1), (4,2), (3,3)))

	if depth - 1 in rgrid:
		grid_above = rgrid[depth - 1]

		if c == 0 and grid_above[2][1] == '#': # left
			alive += 1
		if r == 0 and grid_above[1][2] == '#': # up
			alive += 1
		if c == MAX and grid_above[2][3] == '#': # right
			alive += 1
		if r == MAX and grid_above[3][2] == '#': # down
			alive += 1

	for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
		rr, cc = (r + dr, c + dc)

		if 0 <= rr < N and 0 <= cc < N:
			if (r, c) == (2, 2):
				continue

			if curgrid[rr][cc] == '#':
				alive += 1

	if curgrid[r][c] == '#':
		if alive == 1:
			return '#'
		return '.'

	if alive == 1 or alive == 2:
		return '#'
	return '.'


def download_input_data():
    global fin
    advent.setup(2019, 24, dry_run=False)
    fin = advent.get_input()

def part01():
    global orig_grid
    global ROWS
    global  COLS
    global MAXROW
    global EMPTY
    global BUG


    orig_grid = list(list(l.strip()) for l in fin)
    ROWS = len(orig_grid)
    COLS = len(orig_grid[0])
    MAXROW = ROWS - 1
    MAXCOL = COLS - 1
    EMPTY, BUG = 0, 1
    

    for r, c in product(range(ROWS), range(COLS)):
        orig_grid[r][c] = BUG if orig_grid[r][c] == '#' else EMPTY

    grid = deepcopy(orig_grid)
    seen = set()

    while True:
        state = tuple(map(tuple, grid))
        if state in seen:
            break

        seen.add(state)
        grid = nextgen(grid)

    total, biodiv = 0, 1
    for r, c in product(range(ROWS), range(COLS)):
        if grid[r][c] == BUG:
            total += biodiv
        biodiv <<= 1

    assert total == 32523825
    advent.submit_answer(1, total)

def part02():
    global N
    global MAX
    N = 5
    MAX = 4

    empty_grid = [['.']*N for _ in range(N)]
    empty_grid[2][2] = '?'

    grid = deepcopy(orig_grid)
    grid[2][2] = '?'

    rgrid = {0: grid}


    for generation in range(1, 200+1):
        newrgrid = deepcopy(rgrid)

        prev_depths = tuple(rgrid.keys())
        d, D = min(prev_depths) - 1, max(prev_depths) + 1

        grid = recursive_nextgen(empty_grid, rgrid, d)

        if any(any(x == '#' for x in row) for row in grid):
            newrgrid[d] = grid

        grid = recursive_nextgen(empty_grid, rgrid, D)
        # dump_char_matrix(grid)
        if any(any(x == '#' for x in row) for row in grid):
            newrgrid[D] = grid

        for depth in prev_depths:
            newrgrid[depth] = recursive_nextgen(rgrid[depth], rgrid, depth)

        rgrid = newrgrid

    bugs = 0
    for grid in rgrid.values():
        bugs += sum(sum(c == '#' for c in row) for row in grid)

    print(bugs)
    advent.submit_answer(2, 2052)

if __name__ == "__main__":
    download_input_data()
    timer_start()
    part01()
    part02()
