def read_next(*args):
	for arg in args:
		for i in arg:
			yield i


for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
	print(item, end='')
