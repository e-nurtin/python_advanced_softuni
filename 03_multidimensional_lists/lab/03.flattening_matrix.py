matrix = []
rows = int(input())

[matrix.extend([int(x) for x in input().split(', ')]) for i in range(rows)]

print(matrix)
