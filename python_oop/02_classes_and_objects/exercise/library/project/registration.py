class Registration:
	def add_user(self, user, library):
		if not any([user.user_id == x.user_id for x in library.user_records]):
			library.user_records.append(user)
		else:
			return f"User with id = {user.user_id} already registered in the library!"
			
	def remove_user(self, user, library):
		if any([user.username == x.username for x in library.user_records]):
			library.user_records = [x for x in library.user_records if x.username != user.username]
		else:
			return "We could not find such user to remove!"
		
	def change_username(self, user_id, new_username, library):
		for user in library.user_records:
			if user.user_id == user_id:
				
				if user.username == new_username:
					return f"Please check again the provided username - it should be different than the username used so far!"
				
				if user.username in library.rented_books:
					library.rented_books[new_username] = library.rented_books.pop(user.username)
					
				user.username = new_username
				
				return f"Username successfully changed to: {new_username} for user id: {user_id}"
				
		return f"There is no user with id = {user_id}!"