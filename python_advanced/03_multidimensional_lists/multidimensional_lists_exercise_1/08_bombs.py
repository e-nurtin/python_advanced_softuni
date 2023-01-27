square = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(square)]
bombs = [tuple(int(y) for y in x.split(',')) for x in input().split()]

moves = (
	(0, 1),   # right
	(0, -1),  # left
	(1, 0),   # down
	(1, 1),   # down-right
	(1, -1),  # down-left
	(-1, 0),  # up
	(-1, 1),  # up-right
	(-1, -1),  # up-left
	(0, 0)    # current position. it should be last.
)

for row, col in bombs:
	if matrix[row][col] <= 0:
		continue
		
	bomb_strength = matrix[row][col]
	for r, c in moves:
		r, c = row + r, col + c

		if 0 <= r < square and 0 <= c < square:
			matrix[r][c] -= bomb_strength if matrix[r][c] > 0 else 0
		
alive_cells = [num for row in range(square) for num in matrix[row] if num > 0]


print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")

[print(*matrix[row]) for row in range(square)]
# [print(' '.join([str(el) for el in row])) for row in matrix]
# for row in matrix:
# 	print(' '.join([str(x) for x in row]))
