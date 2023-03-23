class cache:
	log = {}
	
	def __init__(self, function):
		self.function = function
	
	def __call__(self, n):
		result = self.function(n)
		self.log[n] = result
		self.function.log = self.log
		return result


@cache
def fibonacci(n):
	if n < 2:
		
		return n
	
	else:
		
		return fibonacci(n - 1) + fibonacci(n - 2)


# def cache(func):
# 	def wrapper(n):
# 		result = func(n)
# 		cache_result[n] = result
# 		return result
#
# 	return wrapper

#
# cache_result = {}
# fibonacci.log = cache_result
# fibonacci(4)
# print(fibonacci.log)
