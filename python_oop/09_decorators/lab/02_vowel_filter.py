def vowel_filter(function):
	def wrapper():
		vowels = "aoueiy"
		return [el for el in function() if el.lower() in vowels]
	
	return wrapper


@vowel_filter
def get_letters():
	return ["a", "b", "c", "d", "e"]


@vowel_filter
def get_aa():
	return "decorators0"


print(get_letters())
print(get_aa())
