def fibonacci():  # Infinite fibonacci generator
	n1, n2 = 0, 1
	while True:
		yield n1
		n1, n2 = n2, n1 + n2


generator = fibonacci()
for i in range(15):
	print(next(generator))
