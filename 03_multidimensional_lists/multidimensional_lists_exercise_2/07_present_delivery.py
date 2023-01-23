# total_presents = int(input())
# n = int(input())
#
# santa_pos, matrix = [], []
# count_nice_kids, happy_nice_kids = 0, 0
#
# directions = {
# 	'up': (-1, 0),
# 	'down': (1, 0),
# 	'left': (0, -1),
# 	'right': (0, 1),
# }
#
# for r in range(n):
# 	matrix.append(input().split())
# 	for c in range(n):
# 		if matrix[r][c] == "S":
# 			santa_pos = [r, c]
# 		elif matrix[r][c] == "V":
# 			count_nice_kids += 1
#
# command = input()
# while command != 'Christmas morning':
#
# 	matrix[santa_pos[0]][santa_pos[1]] = '-'
# 	r, c = santa_pos[0] + directions[command][0], santa_pos[1] + directions[command][1]
# 	#
# 	# if not (0 <= r < n and 0 <= c < n):
# 	# 	continue
# 	santa_pos = [r, c]
#
# 	if matrix[r][c] == "V":
# 		happy_nice_kids += 1
# 		total_presents -= 1
#
# 	elif matrix[r][c] == "C":
#
# 		for row, col in directions.values():
# 			row, col = santa_pos[0] + row, santa_pos[1] + col
#
# 			if matrix[row][col] == 'V':
# 				total_presents -= 1
# 				happy_nice_kids += 1
#
# 			elif matrix[row][col] == 'X':
# 				total_presents -= 1
#
# 			matrix[row][col] = '-'
#
# 	matrix[r][c] = 'S'
#
# 	if total_presents == 0:
# 		print("Santa ran out of presents!")
# 		break
#
# 	command = input()
#
# [print(' '.join(row)) for row in matrix]
#
# if count_nice_kids == happy_nice_kids:
# 	print(f"Good job, Santa! {happy_nice_kids} happy nice kid/s.")
# else:
# 	print(f"No presents for {count_nice_kids - happy_nice_kids} nice kid/s.")
#
