def check_borders(row, col, way):
	row, col = row + directions[way][0],  col + directions[way][1]
	if row < 0:
		row = square_n - 1
	elif row == len(matrix):
		row = 0
	if col < 0:
		col = square_n - 1
	elif col == len(matrix):
		col = 0
	
	return row, col


def check_path(row, col, curr_coins, hit_a_wall=False):
	element = matrix[row][col]
	matrix[row][col] = ' '
	
	if element == "X":
		hit_a_wall = True
	elif element.isdigit():
		curr_coins += int(element)
		
	path.append([row, col])
	
	return curr_coins, matrix, hit_a_wall


square_n = int(input())

coins = 0
path, matrix = [], []

directions = {
	'up': (-1, 0),
	'down': (1, 0),
	'left': (0, -1),
	'right': (0, 1),
}

for r in range(square_n):
	matrix.append(input().split())
	if "P" in matrix[r]:
		path.append([r, matrix[r].index('P')])

command = input()
while command:
	
	if command in directions:
		r, c = check_borders(path[-1][0], path[-1][1], command)
		coins, matrix, hit_wall = check_path(r, c, coins)
	
		if hit_wall:
			coins = coins // 2
			print(f"Game over! You've collected {coins} coins.")
			break
			
		elif coins >= 100:
			print(f"You won! You've collected {coins} coins.")
			break
	
	command = input()

print("Your path:")
[print(step) for step in path]
