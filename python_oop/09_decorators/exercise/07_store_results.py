class store_results:
	def __init__(self, function):
		self.function = function
	
	def __call__(self, *args):
		result = f"Function '{self.function.__name__}' was called. Result: {self.function(*args)}\n"
		
		with open('results.txt', 'a') as file:
			file.writelines(result)


# def store_results(func):
# 	def wrapper(*args):
# 		result = f"Function '{func.__name__}' was called. Result: {func(*args)}\n"
#
# 		with open('results.txt', 'a') as file:
# 			file.writelines(result)
#
# 	return wrapper

@store_results
def add(a, b):
	return a + b


@store_results
def mult(a, b):
	return a * b


add(2, 2)
mult(6, 4)
