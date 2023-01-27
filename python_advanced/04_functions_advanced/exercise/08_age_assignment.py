def age_assignment(*args, **kwargs):
	result = []
	
	for name in args:
		result.append(f"{name} is {kwargs[name[0]]} years old.")
	
	return '\n'.join(sorted(result))
