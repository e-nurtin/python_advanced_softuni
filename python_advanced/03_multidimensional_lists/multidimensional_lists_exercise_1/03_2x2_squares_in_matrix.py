rows, columns = list(map(int, input().split()))
matrix = [input().split() for x in range(rows)]

equal_cubes = 0

for row in range(rows - 1):
	for col in range(columns - 1):
		symbol = matrix[row][col]
		
		if matrix[row + 1][col] == symbol \
			and matrix[row][col + 1] == symbol \
			and matrix[row + 1][col + 1] == symbol:
			
			equal_cubes += 1

print(equal_cubes)

# rows, columns = list(map(int, input().split()))
# matrix = [input().split() for x in range(rows)]
#
# moves = [(0, 0), (0, 1), (1, 1), (1, 0)]
# equal_cubes = 0
#
# for r in range(rows - 1):
# 	for c in range(columns - 1):
# 		current_cube = []
# 		for i in range(len(moves)):
# 			current_cube.append(matrix[r + moves[i][0]][c + moves[i][1]])
#
# 		if current_cube.count(current_cube[0]) == 4:
# 			equal_cubes += 1
#
# print(equal_cubes)
