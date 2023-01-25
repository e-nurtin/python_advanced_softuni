from collections import deque


def math_operations(*args, **kwargs):
	element = 1
	numbers_ = deque(args)
	while numbers_:
		current_number = float(numbers_.popleft())
		
		if element == 1:
			kwargs['a'] += current_number
		elif element == 2:
			kwargs['s'] -= current_number
		elif element == 3:
			if current_number:
				kwargs['d'] /= current_number
		elif element == 4:
			kwargs['m'] *= current_number
		
		element += 1
		if element > 4:
			element = 1
		
	sorted_d = sorted(kwargs.items(), key=lambda x:(-x[1], x[0]))
	result = [f"{key}: {value:.1f}" for key, value in sorted_d]
	return '\n'.join(result)
