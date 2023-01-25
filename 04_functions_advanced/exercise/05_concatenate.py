def concatenate(*args, **kwargs):
	result = ''
	for substring in args:
		result += substring
	
	for key, value in kwargs.items():
		if key in result:
			result = result.replace(key, value)
			
	return result
