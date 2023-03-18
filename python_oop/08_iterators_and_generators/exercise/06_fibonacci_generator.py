def fibonacci():  # Infinite fibonacci generator
	num = 0
	sequence = [0, 1]
	while True:
		if num < 2:
			yield num
			num += 1
		else:
			next_n = sequence[-2] + sequence[-1]
			yield next_n
			sequence.append(next_n)


generator = fibonacci()
for i in range(15):
	print(next(generator))
