class Library:
	def __init__(self):
		self.user_records = []
		self.books_available = {}
		self.rented_books = {}
		
	def get_book(self, author, book_name, days_to_return, user):
		if author in self.books_available:
			if book_name in self.books_available[author]:
				self.rented_books[user] = {}
				self.rented_books[user][book_name] = days_to_return
				self.books_available[author].remove(book_name)
				self.user_records.append(user)
		
	
	def return_book(self, author, book_name, user):
		pass