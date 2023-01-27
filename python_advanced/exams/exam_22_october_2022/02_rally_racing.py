square_n = int(input())
car_number = input()

distance_covered = 0
matrix, tunnel_pos = [], []
car_pos = [0, 0]

directions = {
	'up': (-1, 0),
	'down': (1, 0),
	'left': (0, -1),
	'right': (0, 1),
}

for row in range(square_n):
	matrix.append(input().split())
	
	if 'T' in matrix[row]:
		tunnel_pos.append((row, matrix[row].index('T')))

while True:
	command = input()
	
	if command == "End":
		print(f"Racing car {car_number} DNF.")
		break
	
	matrix[car_pos[0]][car_pos[1]] = '.'
	r, c = car_pos[0] + directions[command][0], car_pos[1] + directions[command][1]
	element = matrix[r][c]

	car_pos = [r, c]
	
	distance_covered += 10

	if element == 'T':
		distance_covered += 20
		car_pos = [tunnel_pos[1][0], tunnel_pos[1][1]]
		matrix[tunnel_pos[0][0]][tunnel_pos[0][1]] = '.'
		
	elif element == 'F':
		print(f"Racing car {car_number} finished the stage!")
		break

matrix[car_pos[0]][car_pos[1]] = 'C'

print(f"Distance covered {distance_covered} km.")
[print(''.join(row)) for row in matrix]
