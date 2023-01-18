rows = int(input())
matrix = [list(input()) for row in range(rows)]

symbol = input()

result = f"{symbol} does not occur in the matrix"

for row in range(rows):
	for col in range(rows):
		if matrix[row][col] == symbol:
			
			result = f"({row}, {col})"
			break
			
	if symbol not in result:
		break
	
print(result)
