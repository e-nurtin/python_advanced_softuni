symbols_to_replace = {"-", ",", ".", "!", "?"}

with open('text.txt') as file:
	lines = file.readlines()

	for line in range(0, len(lines), 2):
		current_line = lines[line]
		for symbol in symbols_to_replace:
			current_line = current_line.replace(symbol, '@')

		result = current_line.split()[::-1]
		print(*result)

