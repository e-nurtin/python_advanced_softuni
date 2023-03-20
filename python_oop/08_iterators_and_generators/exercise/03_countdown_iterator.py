class countdown_iterator:
	def __init__(self, number):
		self.n = number
		self.i = -1
	
	def __iter__(self):
		return self
	
	def __next__(self):
		if self.n <= self.i:
			raise StopIteration
		
		self.i += 1
		return self.n - self.i


iterator = countdown_iterator(10)
for item in iterator:
	print(item, end=" ")
