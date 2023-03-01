class Band:
	def __init__(self, name):
		self.name = name
		self.albums = []
	
	def add_album(self, album):
		if album in self.albums:
			return f"Band {self.name} already has {album.name} in their library."
		
		self.albums.append(album)
		return f"Band {self.name} has added their newest album {album.name}."
	
	def remove_album(self, album_name):
		if not any([album_name == x.name for x in self.albums]):
			return f"Album {album_name} is not found."
		
		elif any([album_name == x.name and x.published for x in self.albums]):
			return "Album has been published. It cannot be removed."
		
		# for name in self.albums:
		# 	if name == album_name:
		# 		self.albums.remove(name)
		# 		break
		[self.albums.remove(x) for x in self.albums if x.name == album_name]
		return f"Album {album_name} has been removed."
	
	def details(self):
		result = [f"Band {self.name}"]
		
		for album in self.albums:
			result.append(f"{album.details()}")
		
		return '\n'.join(result)
