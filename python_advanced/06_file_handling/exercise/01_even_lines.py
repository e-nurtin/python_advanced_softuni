symbols_to_replace = {"-", ",", ".", "!", "?"}

with open('text.txt') as file:
	lines = file.readlines()

	for line in range(len(lines)):

		if line % 2 == 0:
			current_line = lines[line]

			for symbol in symbols_to_replace:
				current_line = current_line.replace(symbol, '@')

			result = current_line.split()[::-1]
			print(*result)

