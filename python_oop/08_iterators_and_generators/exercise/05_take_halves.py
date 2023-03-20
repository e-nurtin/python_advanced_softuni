def solution():
	def integers():
		num = 1
		
		while True:
			yield num
			num += 1

	def halves():
		for i in integers():
			yield i / 2
	
	def take(n, seq):
		return [next(seq) for _ in range(n)]
	
	return (take, halves, integers)


take = solution()[0]
halves = solution()[1]
print(take(15, halves()))

take = solution()[0]
halves = solution()[1]
integers = solution()[2]
print(take(10, integers()))
