
board = set()
new_board = []

def neighbours(point):
	''' takes a touple in the form (x,y) as an input and  returns all its 
	neigbours sequentally'''
	for x in range(-1,2):
		for y in range(-1,2):
			if (x,y) != (0,0):
				yield (point[0] + x, point[1] + y)

def spawn(point):
	global new_board
	alive_neighbours = 0
	if point not in board:
		for neighbour in neighbours(point):
			if neighbour in board:
				alive_neighbours += 1
	if alive_neighbours == 3:
		new_board.append(point)
		return True
	return False
	
def die(point):
	global new_board
	alive_neighbours = 0
	if point in board:
		for neighbour in neighbours(point):
			if neighbour in board:
				alive_neighbours += 1

	if 1 < alive_neighbours < 4:

		new_board.append(point)
		return False
	
	return True

def run():
	global board
	global new_board
	i = 0
	while board:
		print(board)
		print("step",i)
		i += 1
		for pt in board:
			for neighbour in neighbours(pt):
				if neighbour not in board:
					spawn(neighbour)
			die(pt)
		board = set(new_board)
		new_board = []




if __name__ == '__main__':
	#init = [(1,1), (2,1),(3,1)]
	init = [(1,1),(0,1),(3,1)]
	for pt in init:
		board.add(pt)

	run()	
