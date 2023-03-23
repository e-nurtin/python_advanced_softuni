from time import time


def exec_time(func):
	def wrapper(*args):
		start_time = time()
		func(*args)
		end_time = time()
		
		return f"{end_time - start_time} for function - {func.__name__}"
	
	return wrapper


@exec_time
def loop(start, end):
	total = 0
	for x in range(start, end):
		total += x
	return total


print(loop(1, 1_000_000))
