BOARD_SIZE = 8
matrix, queen_positions, king_pos = [], [], ()
queens_that_can_move = []

directions = {
	'up': (-1, 0),
	'down': (1, 0),
	'left': (0, -1),
	'right': (0, 1),
	'up-left': (-1, -1),
	'up-right': (-1, 1),
	'down-left': (1, -1),
	'down-right': (1, 1),
}

for r in range(BOARD_SIZE):
	matrix.append(input().split())
	
	for c in range(BOARD_SIZE):
		
		if matrix[r][c] == 'Q':
			queen_positions.append((r, c))
		elif matrix[r][c] == "K":
			king_pos = (r, c)


for queen in queen_positions:
	
	for way in directions.values():
		r, c = queen[0], queen[1]
		
		for i in range(BOARD_SIZE):
			r, c = r + way[0], c + way[1]
		
			if not (0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE):
				break
				
			element = matrix[r][c]
			
			if element == 'Q':
				break
			elif element == 'K':
				queens_that_can_move.append([queen[0], queen[1]])
	
				
if not queens_that_can_move:
	print("The king is safe!")
else:
	print(*queens_that_can_move, sep='\n')
	