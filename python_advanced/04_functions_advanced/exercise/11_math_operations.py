def math_operations(*numbers, **kwargs):

	for i in range(len(numbers)):
		
		key = list(kwargs.keys())[i % 4]

		if key == 'a':
			kwargs[key] += numbers[i]
		elif key == 's':
			kwargs[key] -= numbers[i]
		elif key == 'd':
			if numbers[i]:
				kwargs[key] /= numbers[i]
		elif key == 'm':
			kwargs[key] *= numbers[i]

	sorted_d = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))
	result = [f"{key}: {value:.1f}" for key, value in sorted_d]
	
	return '\n'.join(result)
