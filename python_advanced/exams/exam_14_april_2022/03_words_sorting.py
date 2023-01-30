def words_sorting(*args):
	
	words_with_ascii_sum = {}
	total_sum = 0
	
	for word in args:
		current_sum = sum([ord(letter) for letter in word])
		total_sum += current_sum
		
		words_with_ascii_sum[word] = current_sum
		
	result = []
	
	if total_sum % 2 == 0:
		sorted_words = dict(sorted(words_with_ascii_sum.items(), key=lambda x: x[0]))
	else:
		sorted_words = dict(sorted(words_with_ascii_sum.items(), key=lambda x: -x[1]))
	
	for word, value in sorted_words.items():
		result.append(f"{word} - {value}")
		
	return '\n'.join(result)
