def tags(tag):
	def decorator(function):
		def wrapper(*args):
			result = f"<{tag}>{function(*args)}</{tag}>"
			
			return result
		
		return wrapper
	
	return decorator
