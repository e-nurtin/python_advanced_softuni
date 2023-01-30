def check_borders(row, col):
	if 0 > row:
		return row + square_n, col
	elif 0 > col:
		return row, col + square_n
	elif row >= square_n:
		return row - square_n, col
	elif col >= square_n:
		return row, col - square_n
	else:
		return row, col


square_n = 6
matrix = []
rover_pos = []

resources_found = {}

for row in range(square_n):
	matrix.append(input().split())
	if 'E' in matrix[row]:
		rover_pos = [row, matrix[row].index('E')]

directions = {
	'up': (-1, 0),
	'down': (1, 0),
	'left': (0, -1),
	'right': (0, 1),
}

commands = input().split(', ')

for way in commands:
	j, k = rover_pos[0] + directions[way][0], rover_pos[1] + directions[way][1]
	r, c = check_borders(j, k)
	
	element = matrix[r][c]
	rover_pos = [r, c]
	
	if element == "R":
		print(f"Rover got broken at ({r}, {c})")
		break
		
	elif element == '-':
		continue
		
	else:
		if element == "W":
			resources_found[element] = resources_found.get(element, 0) + 1
			element = "Water"
			
		elif element == "M":
			resources_found[element] = resources_found.get(element, 0) + 1
			element = "Metal"
			
		elif element == "C":
			resources_found[element] = resources_found.get(element, 0) + 1
			element = "Concrete"
			
		print(f"{element} deposit found at ({r}, {c})")

if all([True if x in resources_found.keys() else False for x in ["W", "C", "M"]]):
	print("Area suitable to start the colony.")
else:
	print("Area not suitable to start the colony.")
		

