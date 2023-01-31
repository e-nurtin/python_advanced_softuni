with open('numbers.txt', 'r') as file:
	print(sum([int(line) for line in file]))
	