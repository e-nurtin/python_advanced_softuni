class sequence_repeat:
	def __init__(self, sequence, count):
		self.sequence = sequence
		self.count = count
		self.i = 0
		self.end = len(sequence)
		
	def __iter__(self):
		return self
	
	def __next__(self):
		if not self.i < self.count:
			raise StopIteration()
		
		current_el = self.sequence[self.i % self.end]
		self. i += 1
		return current_el
	
	
# result = sequence_repeat('abc', 5)
# for item in result:
#     print(item, end ='')
result = sequence_repeat('I Love Python', 3)
for item in result:
	print(item, end='')
