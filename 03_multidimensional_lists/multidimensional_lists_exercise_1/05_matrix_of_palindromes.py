rows, columns = [int(x) for x in input().split()]

matrix = []

for r in range(rows):
	matrix.append([])

	for c in range(columns):
		first_last = chr(97 + r)
		mid = chr(97 + r + c)

		matrix[r].append(f"{first_last}{mid}{first_last}")

	print(' '.join([x for x in matrix[r]]))


#
# rows, columns = [int(x) for x in input().split()]
# matrix = [[f"{chr(97 + r)}{chr(97 + r + c)}{chr(97 + r)}" for c in range(columns)] for r in range(rows)]
# [print(*row) for row in matrix]
