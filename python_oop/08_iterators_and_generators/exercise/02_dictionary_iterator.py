class dictionary_iter:
	def __init__(self, obj_dict: dict):
		self.obj_dict = tuple(obj_dict.items())
		self.end = len(obj_dict)
		self.i = 0
	
	def __iter__(self):
		return self
	
	def __next__(self):
		if self.i < self.end:
			current_item = self.obj_dict[self.i]
			self.i += 1
			return current_item
		else:
			raise StopIteration()


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
	print(x)

result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
	print(x)
