def valid_index(row, column, move):
	if row + move[0] < len(matrix) and column + move[1] < len(matrix[0]):
		return True
	return False


rows, columns = list(map(int, input().split()))
matrix = [list(input().split()) for x in range(rows)]

moves = [(0, 0), (0, 1), (1, 1), (1, 0)]
equal_cubes = 0

for r in range(rows - 1):
	for c in range(columns - 1):
		current_cube = []
		for i in range(len(moves)):
			if valid_index(r, c, moves[i]):
				current_cube.append(matrix[r + moves[i][0]][c + moves[i][1]])

		if current_cube.count(current_cube[0]) == 4:
			equal_cubes += 1

print(equal_cubes)
