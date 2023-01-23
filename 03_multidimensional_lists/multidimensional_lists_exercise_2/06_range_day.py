def valid_index(x, y):
	if 0 <= x < size and 0 <= y < size:
		return True
	return False


def move_player(player_pos, data):
	direction, steps = data[0], int(data[1])
	
	step = [x * steps if x != 0 else 0 for x in directions[direction]]
	r, c = player_pos[0] + step[0], player_pos[1] + step[1]
	
	if not valid_index(r, c):
		return player_pos
	if matrix[r][c] == 'x':
		return player_pos
	
	return [r, c]


def shoot_target(player_pos, direction):
	r, c = player_pos[0], player_pos[1]
	
	for _ in range(size):
		r, c = r + directions[direction][0], c + directions[direction][1]
		
		if valid_index(r, c):
			if matrix[r][c] == "x":
				shot_targets.append([r, c])
				matrix[r][c] = '.'
				break
		else:
			break


size = 5
matrix, shooter_pos, shot_targets = [], [], []
count_targets = 0

directions = {
	'up': (-1, 0),
	'down': (1, 0),
	'left': (0, -1),
	'right': (0, 1),
}

for row in range(size):
	matrix.append(input().split())
	
	for col in range(size):
		if matrix[row][col] == 'x':
			count_targets += 1
		
		elif matrix[row][col] == "A":
			matrix[row][col] = '.'
			shooter_pos = [row, col]

for _ in range(int(input())):
	command, *info = input().split()
	
	if command == "shoot":
		shoot_target(shooter_pos, info[0])
	
	elif command == "move":
		shooter_pos = move_player(shooter_pos, info)

if len(shot_targets) == count_targets:
	print(f"Training completed! All {count_targets} targets hit.")
else:
	print(f"Training not completed! {count_targets - len(shot_targets)} targets left.")

# [print(target) for target in shot_targets]
print(*shot_targets, sep='\n')
