rows, columns = [int(x) for x in input().split()]
matrix, base_pos = [], []
moves_made, players_touched = 0, 0

directions = {
	'up': (-1, 0),
	'down': (1, 0),
	'left': (0, -1),
	'right': (0, 1),
}

for row in range(rows):
	matrix.append(input().split())
	if 'B' in matrix[row]:
		base_pos = [row, matrix[row].index('B')]


while players_touched < 3:
	command = input()
	
	if command == 'Finish':
		break
		
	r, c = base_pos[0] + directions[command][0], base_pos[1] + directions[command][1]
	
	if not (0 <= r < rows and 0 <= c < columns):
		continue
	
	element = matrix[r][c]
	
	if element == 'O':
		continue
		
	elif element == 'P':
		matrix[r][c] = '-'
		players_touched += 1
			
	moves_made += 1
	base_pos = [r, c]
	
	
print("Game over!")
print(f"Touched opponents: {players_touched} Moves made: {moves_made}")
