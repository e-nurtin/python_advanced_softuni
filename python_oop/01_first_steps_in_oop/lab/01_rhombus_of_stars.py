def print_row(figure_size, row_size):
	return f"{' ' * (figure_size - row_size)}{'* ' * row_size}"


n = int(input())

for row in range(1, n + 1):
	print(print_row(n, row))

for row in range(n - 1, 0, -1):
	print(print_row(n, row))
