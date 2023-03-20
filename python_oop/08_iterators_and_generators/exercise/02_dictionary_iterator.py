class dictionary_iter:
	def __init__(self, obj_dict: dict):
		self.items = tuple(obj_dict.items())
		self.i = -1
	
	def __iter__(self):
		return self
	
	def __next__(self):
		if self.i >= len(self.items) - 1:
			raise StopIteration
		
		self.i += 1
		return self.items[self.i]


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
	print(x)

result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
	print(x)
