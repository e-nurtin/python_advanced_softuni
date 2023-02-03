def flights(*args):
	data = {}
	for i in range(0, len(args), 2):
		if args[i] == "Finish":
			break
			
		if args[i] not in data:
			data[args[i]] = 0
		data[args[i]] += int(args[i + 1])
		
	return data
