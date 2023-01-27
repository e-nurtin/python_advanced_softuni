size = int(input())
commands = input().split()

matrix = []
miner_pos = []
total_coal = 0

directions = {
	'up': (-1, 0),
	'down': (1, 0),
	'left': (0, -1),
	'right': (0, 1),
}

for row in range(size):
	matrix.append(input().split())
	if 's' in matrix[row]:
		miner_pos = [row, matrix[row].index('s')]
		matrix[row][miner_pos[1]] = '*'
	
	total_coal += matrix[row].count('c')

for move in commands:
	r, c = miner_pos[0] + directions[move][0], miner_pos[1] + directions[move][1]
	
	if not (0 <= r < size and 0 <= c < size):
		continue
	
	miner_pos = [r, c]
	
	if matrix[r][c] == 'c':
		total_coal -= 1
		
		if total_coal == 0:
			print(f"You collected all coal! ({r}, {c})")
			break
	
	elif matrix[r][c] == 'e':
		print(f"Game over! ({r}, {c})")
		break
	
	matrix[r][c] = '*'
	
else:
	print(f"{total_coal} pieces of coal left. ({miner_pos[0]}, {miner_pos[1]})")

#
#
# def valid_index(miner, step):
# 	if 0 <= miner[0] + step[0] < len(field) and 0 <= miner[1] + step[1] < len(field):
# 		return True
# 	return False
#
#
# def change_position(miner, step, coal):
# 	if valid_index(miner, step):
# 		pos = [miner[0] + step[0], miner[1] + step[1]]
# 		field[miner[0]][miner[1]] = '*'
# 		miner = pos
#
# 		if field[pos[0]][pos[1]] == 'c':
# 			coal -= 1
# 			field[pos[0]][pos[1]] = 's'
#
# 		elif field[pos[0]][pos[1]] == 'e':
# 			coal = -1
#
# 	return miner, coal
#
#
# field_size = int(input())
# move_commands = input().split()
#
# field = [[x for x in input().split()] for _ in range(field_size)]
# miner_position = []
# total_coal = 0
#
# moves = {
# 	'left': (0, -1),
# 	'right': (0, 1),
# 	'up': (-1, 0),
# 	'down': (1, 0),
# }
#
# for r in range(field_size):
# 	for c in range(field_size):
# 		if field[r][c] == 's':
# 			miner_position = [r, c]
# 		elif field[r][c] == 'c':
# 			total_coal += 1
#
#
# for move in move_commands:
# 	miner_position, total_coal = change_position(miner_position, moves[move], total_coal)
#
# 	if total_coal == 0:
# 		print(f"You collected all coal! ({miner_position[0]}, {miner_position[1]})")
# 		break
#
# 	elif total_coal == -1:
# 		print(f"Game over! ({miner_position[0]}, {miner_position[1]})")
# 		break
#
# else:
# 	print(f"{total_coal} pieces of coal left. ({miner_position[0]}, {miner_position[1]})")
#
