def forecast(*args):
	list_to_sort = [arg for arg in args]
	sorted_list = sorted(list_to_sort, key=lambda x: ('Rainy' in x, 'Cloudy' in x, 'Sunny' in x, x))
	
	result = []
	for city, weather in sorted_list:
		result.append(f"{city} - {weather}")
		
	return '\n'.join(result)



print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))
