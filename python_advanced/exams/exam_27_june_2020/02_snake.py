matrix_size = int(input())

matrix, snake_pos, burrows = [], [], []
food_eaten = 0

directions = {
	'up': (-1, 0),
	'down': (1, 0),
	'left': (0, -1),
	'right': (0, 1),
}

for row in range(matrix_size):
	matrix.append(list(input()))
	for col in range(matrix_size):
		if matrix[row][col] == "S":
			snake_pos = [row, col]
			matrix[row][col] = '.'
		elif matrix[row][col] == "B":
			burrows.append((row, col))

while food_eaten < 10:
	command = input()
	matrix[snake_pos[0]][snake_pos[1]] = '.'
	row, col = snake_pos[0] + directions[command][0], snake_pos[1] + directions[command][1]
	
	if not (0 <= row < matrix_size and 0 <= col < matrix_size):
		matrix[snake_pos[0]][snake_pos[1]] = "."
		break
	
	element = matrix[row][col]
	matrix[row][col] = 'S'
	snake_pos = [row, col]
	
	if element == '*':
		food_eaten += 1
	
	elif element == "B":
		for i in range(len(burrows)):
			if burrows[i] == (row, col):
				matrix[snake_pos[0]][snake_pos[1]] = "."
				burrows.remove((row, col))
				break
		
		snake_pos = burrows.pop()
		matrix[snake_pos[0]][snake_pos[1]] = "S"

	
if food_eaten == 10:
	print("You won! You fed the snake.")
else:
	print("Game over!")

print(f"Food eaten: {food_eaten}")
[print(''.join(row)) for row in matrix]
