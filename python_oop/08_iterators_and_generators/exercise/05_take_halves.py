def solution():
	def integers():
		i = 1
		while True:
			yield i
			i += 1

	def halves():
		for i in integers():
			yield i / 2
	
	def take(n, seq):
		return list((next(seq) for _ in range(n)))
	
	return (take, halves, integers)


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))

take = solution()[0]
halves = solution()[1]
print(take(0, halves()))