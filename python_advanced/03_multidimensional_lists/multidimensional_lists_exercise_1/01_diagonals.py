rows = int(input())
matrix = [[int(x) for x in input().split(', ')] for _ in range(rows)]

primary = []
secondary = []

for i in range(rows):
	primary.append(matrix[i][i])
	secondary.append(matrix[i][rows-1-i])
	
print(f"Primary diagonal: {', '.join([str(x) for x in primary])}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary])}. Sum: {sum(secondary)}")
