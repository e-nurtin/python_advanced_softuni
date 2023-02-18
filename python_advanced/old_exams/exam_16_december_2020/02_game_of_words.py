initial_string = input()
square_n = int(input())

directions = {
	'up': (-1, 0),
	'down': (1, 0),
	'left': (0, -1),
	'right': (0, 1),
}

matrix, player_pos = [], []

for r in range(square_n):
	matrix.append(list(input()))
	
	if 'P' in matrix[r]:
		player_pos = [r, matrix[r].index('P')]
		matrix[r][player_pos[1]] = '-'
		
number_of_moves = int(input())

for _ in range(number_of_moves):
	move = input()
	
	row, col = player_pos[0] + directions[move][0], player_pos[1] + directions[move][1]
	
	if not (0 <= row < square_n and 0 <= col < square_n):
		if initial_string:
			initial_string = initial_string[:-1]
			continue
	
	element = matrix[row][col]
	if element.isalpha():
		initial_string += element
		
	matrix[row][col] = '-'
	player_pos = [row, col]

matrix[player_pos[0]][player_pos[1]] = 'P'

print(initial_string)

[print(''.join(row)) for row in matrix]
