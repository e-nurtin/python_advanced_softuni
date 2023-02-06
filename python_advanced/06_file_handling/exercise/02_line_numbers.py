from string import punctuation


def read_lines(filename='text.txt'):
	with open(filename, 'r') as text_file:
		lines = text_file.readlines()
	
	return lines


def count_alpha_and_punct(text):
	punctuations, alphabet_letters = 0, 0
	
	for char in text:
		if char.isalpha():
			alphabet_letters += 1
			
		elif char in punctuation:
			punctuations += 1
	
	return alphabet_letters, punctuations


def modify_lines(text, count_alpha, count_punct, line_n):
	current_line = text.split()
	current_line.insert(0, f"Line {line_n}:")
	current_line.append(f"({count_alpha})({count_punct})")
	
	return ' '.join(current_line)


def write_mods_to_newfile(text, filename='output.txt'):
	with open(filename, 'w') as file:
		file.writelines('\n'.join(text))


result = []
file_lines = read_lines()

for line in range(len(file_lines)):
	alpha, punct = count_alpha_and_punct(file_lines[line][:-1])
	final_line = modify_lines(file_lines[line], alpha, punct, line + 1)
	
	result.append(final_line)

write_mods_to_newfile(result)
