class Profile:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		
	@property
	def username(self):
		return self.__username
	
	@username.setter
	def username(self, value):
		if len(value) < 5 or len(value) > 15:
			raise ValueError("The username must be between 5 and 15 characters.")
		self.__username = value
		
	@property
	def password(self):
		return self.__password
	
	@password.setter
	def password(self, value):
		valid_length = len(value) >= 8
		has_uppercase = any([True for char in value if char.isupper()])
		has_digit = any([True for char in value if char.isdigit()])
		
		if not (valid_length and has_uppercase and has_digit):
			raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
		self.__password = value

	def __str__(self):
		return f'You have a profile with username: "{self.__username}" and password: {"*" * len(self.__password)}'


#
# from re import search
#
#
# class Profile:
# 	def __init__(self, username, password):
# 		if not 5 <= len(username) <= 15:
# 			raise ValueError("The username must be between 5 and 15 characters.")
# 		self.__username = username
#
# 		if not validate_password(password):
# 			raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
# 		self.__password = password
#
# 	def __str__(self):
# 		return f'You have a profile with username: "{self.__username}" and password: {"*" * len(self.__password)}'
#
#
# def validate_password(password):
# 	if len(password) >= 8 and (search(r'[A-Z]+', password) and search(r'[0-9]+', password)):
# 		return True
# 	return False
#

# profile_with_invalid_password = Profile('My_username', 'My-password')
# profile_with_invalid_username = Profile('Too_long_username', 'Any')
# correct_profile = Profile("Username", "Passw0rd")
# print(correct_profile)
