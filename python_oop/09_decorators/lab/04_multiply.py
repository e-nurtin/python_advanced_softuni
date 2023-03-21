def multiply(times):
	def decorator(function):
		def wrapper(*args):
			result = function(args[0])
			return result * times
		
		return wrapper
	
	return decorator


@multiply(5)
def add_ten(number):
	return number + 10


# a = multiply(3)(add_ten)(5)
print(add_ten(6))
# First, we add 3 to 10 = 13, and then we multiply the result by 3: 13 * 3 = 39
