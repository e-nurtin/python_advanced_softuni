# better way
rows, columns = [int(x) for x in input().split(', ')]

matrix = []
total_sum = 0

for row in range(rows):
	matrix.append([int(x) for x in input().split(', ')])
	total_sum += sum(matrix[row])

print(total_sum)
print(matrix)

# 2 conventional way
#
# rows, columns = [int(x) for x in input().split(', ')]
#
# matrix = []
# total_sum = 0
# for row in range(rows):
# 	matrix.append([])
# 	current_column = [int(x) for x in input().split(', ')]
# 	for column in current_column:
# 		total_sum += column
# 		matrix[row].append(column)
# print(total_sum)
# print(matrix)
