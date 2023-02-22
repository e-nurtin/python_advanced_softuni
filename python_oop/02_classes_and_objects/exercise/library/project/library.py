class Library:
	def __init__(self):
		self.user_records = []
		self.books_available = {}  # Example {'Harper Lee': ['To Kil a mockingbird', 'Another Book' ..etc]}
		self.rented_books = {}  # Example {"user": {"book name": "days to return"}, "user2":{"book": "days"}...}
	
	def get_book(self, author, book_name, days_to_return, user):
		if author in self.books_available:
			
			if book_name in self.books_available[author]:
				user.books.append(book_name)
				self.books_available[author].remove(book_name)
				
				if user.user_id not in self.rented_books:
					self.rented_books[user.username] = {}
				
				if book_name not in self.rented_books[user.username]:
					self.rented_books[user.username][book_name] = days_to_return
				
				return f"{book_name} successfully rented for the next {days_to_return} days!"
			
		for name, data in self.rented_books.items():
			if book_name in data:
				return f'The book "{book_name}" is already rented and will be available in {data[book_name]} days!'

	def return_book(self, author, book_name, user):
		if book_name in user.books:
			user.books.remove(book_name)
			self.books_available[author].append(book_name)
			del self.rented_books[user.username][book_name]
			
		else:
			return f"{user.username} doesn't have this book in his/her records!"
		