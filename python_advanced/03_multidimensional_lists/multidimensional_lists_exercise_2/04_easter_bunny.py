n = int(input())

bunny_pos, matrix, best_path = [], [], []
max_collected_eggs = 0
best_direction = ''

directions = {
	'up': (-1, 0),
	'down': (1, 0),
	'left': (0, -1),
	'right': (0, 1),
}

for row in range(n):
	matrix.append(input().split())
	for col in range(n):
		if matrix[row][col] == 'B':
			bunny_pos = [row, col]

for direction, step in directions.items():
	r, c = bunny_pos[0] + step[0], bunny_pos[1] + step[1]
	
	eggs_collected = 0
	path = []
	
	while 0 <= r < n and 0 <= c < n:
		
		if matrix[r][c] == "X":
			break
		
		eggs_collected += int(matrix[r][c])
		path.append([r, c])
		
		r, c = r + step[0], c + step[1]
	
	if eggs_collected >= max_collected_eggs:
		max_collected_eggs = eggs_collected
		best_direction = direction
		best_path = path

print(best_direction)
print(*best_path, sep='\n')
print(max_collected_eggs)
