class countdown_iterator:
	def __init__(self, count):
		self.i = count
		self.end = 0
	
	def __iter__(self):
		return self
	
	def __next__(self):
		if self.i >= self.end:
			current_count = self.i
			self.i -= 1
			return current_count
		else:
			raise StopIteration()


iterator = countdown_iterator(10)
for item in iterator:
	print(item, end=" ")
