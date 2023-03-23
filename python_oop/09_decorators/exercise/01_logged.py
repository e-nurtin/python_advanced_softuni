def logged(function):
	def wrapper(*args):
		result = [f"you called {function.__name__}({', '.join([str(i) for i in args])})"]
		
		func_res = function(*args)
		result.append(f"it returned {func_res}")
		
		return '\n'.join(result)
	
	return wrapper


@logged
def func(*args):
	return 3 + len(args)


print(func(4, 4, 4))
