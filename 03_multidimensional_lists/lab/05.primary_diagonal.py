rows = int(input())

matrix = [[int(x) for x in input().split()] for row in range(rows)]

result = sum(matrix[row][row] for row in range(rows))

print(result)


# first variant
#
# rows = int(input())
# matrix = [[int(x) for x in input().split()] for _ in range(rows)]
#
# result = 0
#
# for i in range(rows):
# 	result += matrix[i][i]
# print(result)
