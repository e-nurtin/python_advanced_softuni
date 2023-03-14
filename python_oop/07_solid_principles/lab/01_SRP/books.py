class Book:
	def __init__(self, title, author, genre):
		self.title = title
		self.author = author
		self.genre = genre
		self.page = 0
	
	def turn_page(self, page):
		self.page = page
		
	def __repr__(self):
		return f'Book by "{self.author}" with title "{self.title}" and genre {self.genre}'


class Library:
	def __init__(self):
		self.books = []
	
	def add_book(self, book):
		self.books.append(book)
	
	def find_book(self, title):
		for book in self.books:
			if book.title == title:
				return book


books = [Book('The Hobbit', 'J.R.R. Tolkien', 'Fiction'), Book("To kill a mockingbird", "Harper Lee", 'Literary'),
         Book("Be water my friend", "Shannon Lee", 'Personal Growth')]

library = Library()
for book in books:
	library.add_book(book)
	
found_book = library.find_book('To kill a mockingbird')

print(found_book)