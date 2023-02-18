def start_spring(**kwargs):
	initial_dict = {}
	
	for key, value in kwargs.items():
		if value not in initial_dict:
			initial_dict[value] = []
		initial_dict[value].append(key)
	
	result = []
	
	for key, values in sorted(initial_dict.items(), key= lambda x:(-len(x[1]), x[0])):
		result.append(f"{key}:")
		
		for item in sorted(values):
			result.append(f"-{item}")
			
	return '\n'.join(result)
