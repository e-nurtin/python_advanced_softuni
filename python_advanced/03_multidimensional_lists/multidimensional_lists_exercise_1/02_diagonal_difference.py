rows = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

primary, secondary = [], []

for i in range(rows):
	primary.append(matrix[i][i])
	secondary.append(matrix[i][rows - 1 - i])
	
print(abs(sum(primary) - sum(secondary)))
