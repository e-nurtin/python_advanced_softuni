def add_songs(*args):
	data = {}
	result = []
	for arg in args:
		
		if arg[0] not in data:
			data[arg[0]] = []
			
		data[arg[0]].extend(arg[1])
	
	for song, lyrics in data.items():
		
		if lyrics:
			lyrics = '\n'.join(lyrics)
			result.append(f"- {song}\n{lyrics}\n")
			
		else:
			result.append(f"- {song}\n")
			
	return ''.join(result)



