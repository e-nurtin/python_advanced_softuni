def grocery_store(**kwargs):
	
	ordered_dict = list(sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0])))
	
	result = []
	for name, quantity in ordered_dict:
		result.append(f"{name}: {quantity}")
		
	return '\n'.join(result)

