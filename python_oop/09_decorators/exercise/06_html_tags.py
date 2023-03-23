def tags(tag):
	def decorator(function):
		def wrapper(*args):
			result = f"<{tag}>{function(*args)}</{tag}>"
			
			return result
		
		return wrapper
	
	return decorator


@tags('h1')
def to_upper(text):
	return text.upper()


print(to_upper('hello'))
