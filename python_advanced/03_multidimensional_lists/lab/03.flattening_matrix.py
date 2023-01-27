matrix = []
rows = int(input())

[matrix.extend([int(x) for x in input().split(', ')]) for i in range(rows)]

print(matrix)


# Long version
#
# rows = int(input())
# matrix = []
# for row in range(rows):
# 	matrix.append([int(x) for x in input().split(', ')])
# 
# result = []
# for array in matrix:
# 	result.extend(array)
# print(result)
