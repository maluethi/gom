import gol

def test_neighbours():
	pt = (1,1)

	n = [(0,0), (0,1), (0,2), (1,0), (1,2), (2,0),(2,1),(2,2)]	

	for idx, neigh in enumerate(gol.neighbours(pt)):
		assert(neigh == n[idx])

def test_spawn():
	gol.board.add((0,0))
	gol.board.add((1,0))
	gol.board.add((2,0))
	

	assert(gol.spawn((1,1)))
	assert((1,1) in gol.new_board)

def test_die():
	gol.new_board = set()
	gol.board.add((0,0))
	assert(gol.die((0,0)))
	assert(len(gol.new_board) == 0)

def test_rotor():
	gol.new_board = []
	init = [(1,1),(2,1),(3,1)]
	gol.board = set(init)
	gol.run()



