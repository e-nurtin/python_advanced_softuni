def valid_index(pos_r, pos_c, row_matrix, col_matrix):
	if 0 <= pos_r < row_matrix and 0 <= pos_c < col_matrix:
		return True
	return False


def mutate_bunnies(row_matrix, col_matrix):
	for bunny in bunny_pos.copy():
		
		for row, col in directions.values():
			r, c = bunny[0] + row, bunny[1] + col
			
			if valid_index(r, c, row_matrix, col_matrix):
				matrix[r][c] = "B"
				bunny_pos.append((r, c))


rows, columns = [int(x) for x in input().split()]

matrix, player_pos, bunny_pos = [], [], []
outcome = ""

directions = {
	'U': (-1, 0),
	'D': (1, 0),
	'L': (0, -1),
	'R': (0, 1),
}

for row in range(rows):
	matrix.append(list(input()))
	
	for col in range(columns):
		
		if 'P' in matrix[row][col]:
			player_pos = [row, col]
			matrix[row][col] = '.'
		
		elif 'B' in matrix[row][col]:
			bunny_pos.append((row, col))

commands = list(input())

for move in commands:
	p_r, p_c = player_pos[0] + directions[move][0], player_pos[1] + directions[move][1]
	mutate_bunnies(rows, columns)
	
	if not valid_index(p_r, p_c, rows, columns):
		outcome = f"won: {player_pos[0]} {player_pos[1]}"
		break
	
	elif matrix[p_r][p_c] == "B":
		outcome = f"dead: {p_r} {p_c}"
		break
		
	player_pos = [p_r, p_c]

[print(''.join(row)) for row in matrix]
print(outcome)
