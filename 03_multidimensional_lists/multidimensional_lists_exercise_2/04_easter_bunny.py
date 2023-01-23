n = int(input())

bunny_pos, matrix = [], []
most_eggs = [0, '']

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

	r, c = bunny_pos[0], bunny_pos[1]
	eggs_collected = 0

	for i in range(n):
		r, c = r + step[0], c + step[1]

		if 0 <= r < n and 0 <= c < n:
			if matrix[r][c] == "X":
				break
				
			eggs_collected += int(matrix[r][c])
		else:
			break

	if eggs_collected > most_eggs[0]:
		most_eggs[0] = eggs_collected
		most_eggs[1] = direction
	
# directions[direction].append(eggs_collected)
print(most_eggs[1])
r, c = bunny_pos[0], bunny_pos[1]

for i in range(n):
	r, c = r + directions[most_eggs[1]][0], c + directions[most_eggs[1]][1]

	if not (0 <= r < n and 0 <= c < n):
		break

	print([r, c])

print(most_eggs[0])
