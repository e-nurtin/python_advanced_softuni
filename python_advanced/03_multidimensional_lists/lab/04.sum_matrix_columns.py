rows, columns = [int(x) for x in input().split(', ')]

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

result = [sum(matrix[row][column] for row in range(rows)) for column in range(columns)]

print(*result, sep='\n')


#
# first variant
#
# rows, columns = [int(x) for x in input().split(', ')]
#
# matrix = [[int(x) for x in input().split()] for _ in range(rows)]
#
# for column in range(columns):
# 	current_sum = 0
# 	for row in range(rows):
# 		current_sum += matrix[row][column]
#
# 	print(current_sum)