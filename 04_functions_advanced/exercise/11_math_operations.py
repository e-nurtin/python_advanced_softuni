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


print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(6.0, a=0, s=0, d=5, m=0))
