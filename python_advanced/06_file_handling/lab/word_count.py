import re


def find_searched_words(file_path):
	searched_words = []
	with open(file_path) as word_file:
		searched_words = word_file.read().split()
	return searched_words


def find_word_occurrences(searched_words, file_path):
	count_of_words = {}
	with open(file_path) as input_file:
		text_to_search = input_file.read()
		for word in searched_words:
			match = re.findall(fr"\b{word}\b", text_to_search, re.I)
			count_of_words[word] = count_of_words.get(word, 0) + len(match)
	return count_of_words


def store_result(result, file_path):
	with open(file_path, 'w') as output_file:
		for word, count in sorted(result.items(), key=lambda x: -x[1]):
			output_file.write(f"{word} - {count}\n")


words = find_searched_words('words.txt')
result = find_word_occurrences(words, 'input.txt')
store_result(result, 'output.txt')