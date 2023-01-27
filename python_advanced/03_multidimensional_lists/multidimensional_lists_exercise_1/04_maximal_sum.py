rows, columns = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for row in range(rows)]

max_sum = float('-inf')
largest_3x3 = []

for r in range(rows - 2):
	for c in range(columns - 2):
		
		first_row = matrix[r][c: c + 3]
		second_row = matrix[r + 1][c: c + 3]
		third_row = matrix[r + 2][c: c + 3]
		
		current_sum = sum(first_row) + sum(second_row) + sum(third_row)
		
		if current_sum > max_sum:
			max_sum = current_sum
			largest_3x3 = [first_row, second_row, third_row]

print(f"Sum = {max_sum}")
[print(*row) for row in largest_3x3]
