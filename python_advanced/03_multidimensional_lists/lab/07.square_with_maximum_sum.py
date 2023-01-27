def valid_index(index, r, c):
	if index[0] + r < len(matrix) and index[1] + c < len(matrix[0]):
		return True
	return False


rows, columns = [int(x) for x in input().split(', ')]

matrix = [[int(x) for x in input().split(', ')] for _ in range(rows)]
largest_cube_sum = 0
moves = [(0, 0), (0, 1), (1, 0), (1, 1)]

for row in range(rows - 1):
	for col in range(columns - 1):
		current_cube = []
		current_cube_sum = 0
		for move in range(len(moves)):
			if valid_index(moves[move], row, col):
				current_cube.append(matrix[row + moves[move][0]][col + moves[move][1]])
				current_cube_sum += matrix[row + moves[move][0]][col + moves[move][1]]
				
		if current_cube_sum > largest_cube_sum:
			largest_cube_sum = current_cube_sum
			largest_cube_digits = current_cube
			
print(*largest_cube_digits[:2])
print(*largest_cube_digits[2:])
print(largest_cube_sum)
