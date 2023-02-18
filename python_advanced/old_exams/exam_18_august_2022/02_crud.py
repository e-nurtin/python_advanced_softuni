def create(row, col, value, symbol):
	if symbol == '.':
		matrix[row][col] = value


def update(row, col, value, symbol):
	if symbol != '.':
		matrix[row][col] = value


def delete(row, col):
	matrix[row][col] = '.'


def read(symbol):
	if symbol != '.':
		print(symbol)


matrix = [input().split() for row in range(6)]

curr_pos = input().split()
curr_pos = [int(curr_pos[0][1]), int(curr_pos[1][0])]

directions = {
	'up': (-1, 0),
	'down': (1, 0),
	'left': (0, -1),
	'right': (0, 1),
}

while True:
	command = input()
	if command == "Stop":
		break
	
	action, *info = command.split(', ')
	
	r, c = curr_pos[0] + directions[info[0]][0], curr_pos[1] + directions[info[0]][1]
	curr_pos = [r, c]
	element = matrix[r][c]
	
	if action == "Create":
		create(r, c, info[1], element)
	
	elif action == "Update":
		update(r, c, info[1], element)
	
	elif action == "Delete":
		delete(r, c)
	
	elif action == "Read":
		read(element)

[print(' '.join(row)) for row in matrix]
