from collections import deque

rows, columns = [int(x) for x in input().split()]
snake_name = deque(list(input()))

matrix = []

for row in range(rows):
	matrix.append([])
	
	for col in range(columns):
		current_symbol = snake_name.popleft()
		
		matrix[row].append(current_symbol)
		snake_name.append(current_symbol)
		
	if row % 2 != 0:
		matrix[row] = matrix[row][::-1]

for row in matrix:
	print(''.join(row))
	