matrix_n, bombs_n = int(input()), int(input())

bomb_positions = []
matrix = [[0 for col in range(matrix_n)] for row in range(matrix_n)]

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

for i in range(bombs_n):
	r, c = [int(x) for x in input()[1:-1].split(', ')]
	bomb_positions.append((r, c))
	matrix[r][c] = '*'

for pos in bomb_positions:
	for way in directions.values():
		r, c = pos[0] + way[0], pos[1] + way[1]
		
		if not (0 <= r < matrix_n and 0 <= c < matrix_n):
			continue
		
		if matrix[r][c] != '*':
			matrix[r][c] += 1 if matrix[r][c] < 3 else 0
			

[print(' '.join([str(x) for x in row])) for row in matrix]
