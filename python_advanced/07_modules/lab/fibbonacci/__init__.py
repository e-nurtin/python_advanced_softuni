def print_fibonacci(n):
	result = []
	result.append(0)
	result.append(1)
	for i in range(n - 2):
		result.append(result[-1] + result[-2])
	return result


def locate_number_in_sequence(sequence, number):
	if number in sequence:
		return sequence.index(number)
	return