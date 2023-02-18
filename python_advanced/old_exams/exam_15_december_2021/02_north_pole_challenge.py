def check_borders(x, y):
	if x >= rows:
		x -= rows
	elif x < 0:
		x += rows
	elif y >= columns:
		y -= columns
	elif y < 0:
		y += columns
	return x, y


def move(way, steps, presents, pos):
	target_c, target_r = 0, 0
	for _ in range(steps):
		target_r = pos[0] + directions[way][0]
		target_c = pos[1] + directions[way][1]
		
		target_r, target_c = check_borders(target_r, target_c)
		pos = [target_r, target_c]
		element = matrix[target_r][target_c]
		matrix[target_r][target_c] = 'x'
		
		if element not in '.x':
			
			if element == "G":
				found_presents["Gifts"] += 1
			
			elif element == "C":
				found_presents["Cookies"] += 1
			
			elif element == "D":
				found_presents["Christmas decorations"] += 1
			
			presents -= 1
			
			if presents == 0:
				print("Merry Christmas!")
				break
				
	return [target_r, target_c], presents


rows, columns = [int(x) for x in input().split(', ')]

matrix, my_pos = [], []
total_presents = 0

found_presents = {
	"Christmas decorations": 0,
	"Gifts": 0,
	"Cookies": 0
}

directions = {
	'up': (-1, 0),
	'down': (1, 0),
	'left': (0, -1),
	'right': (0, 1),
}

for row in range(rows):
	matrix.append(input().split())
	for column in range(columns):
		
		if matrix[row][column] == "Y":
			my_pos = [row, column]
			matrix[row][column] = 'x'
			
		elif matrix[row][column] in "GCD":
			total_presents += 1

while True:
	command = input()
	if command == "End":
		break
	
	direction, count = [int(x) if x.isdigit() else x for x in command.split('-')]
	
	my_pos, total_presents = move(direction, count, total_presents, my_pos)
	
	if total_presents == 0:
		break


result = ["You've collected:"]

for present, count in found_presents.items():
	result.append(f"- {count} {present}")
	
print('\n'.join(result))

matrix[my_pos[0]][my_pos[1]] = 'Y'

[print(' '.join(row)) for row in matrix]
