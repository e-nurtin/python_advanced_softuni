class NameTooShortError(Exception):
	pass


class MustContainAtSymbolError(Exception):
	pass


class InvalidDomainError(Exception):
	pass


while True:
	email = input()
	if email == 'End':
		break
	
	if "@" not in email:
		raise MustContainAtSymbolError("Email must contain @")
	
	elif len(email[:email.index('@')]) < 5:
		raise NameTooShortError("Name must be more than 4 characters")
	
	elif not any(email.endswith(x) for x in ('.com', '.bg', '.org', '.net')):
		raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
	
	else:
		print("Email is valid")
	