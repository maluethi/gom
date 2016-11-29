#/bin/python
# little implementation of the 'game of life' inspired by https://youtu.be/o9pEzgHorH0?t=17m57s

import itertools as iter

def neighbours(point):
	x, y = point
	for (x_offset, y_offset) in iter.product(range(-1,2), range(-1,2)):
		if (x_offset, y_offset) == (0, 0):
			continue
		yield (x + x_offset, y + y_offset)


def alive_neighbors(point, board):
	alive = {pt for pt in neighbours(point) if pt in board}
	return len(alive)


def recalc(board):
	new_board = set()
	# check if new life gets born somewhere
	for pt in iter.chain(*map(neighbours, board)):
		if pt not in board and alive_neighbors(pt, board) == 3:
			new_board.add(pt)
	# check who survives
	for pt in board:
		if 1 < alive_neighbors(pt, board) < 4:
			new_board.add(pt)

	return new_board

glider = set([(0,0), (1,0), (2,0), (0,1), (1,2)])
for i in range(1000):
	print("step", i)
	glider = recalc(glider)
	
