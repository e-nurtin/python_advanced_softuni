def console_triangle_from_n(n: int):
	for i in range(n + 1):
		for j in range(1, i + 1):
			print(j, end=' ')
		print()
	for i in range(n-1, 0, -1):
		for j in range(1, i + 1):
			print(j, end=' ')
		print()
