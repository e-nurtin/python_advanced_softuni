def even_odd_filter(**kwargs):
	for key in kwargs:
		if key == 'even':
			kwargs[key] = [int(x) for x in kwargs[key] if int(x) % 2 == 0]
		else:
			kwargs[key] = [int(x) for x in kwargs[key] if int(x) % 2 != 0]
			
	ordered_dict = {i[0]: i[1] for i in sorted(kwargs.items(), key=lambda x: -len(x[1]))}
	
	return ordered_dict
