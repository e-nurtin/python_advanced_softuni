class Book:
	def __init__(self, content: str, title: str, author: str):
		self.title = title
		self.author = author
		self.content = content


class Formatter:
	@staticmethod
	def format(book: Book) -> str:
		return book.content


class FancyFlyer:
	@staticmethod
	def format(book: Book) -> str:
		return f"{'-' * 10}\n{book.title}\n{'-' * 10}\n{book.author}\n{'-' * 10}"


class Printer:
	def __init__(self, formatter):  # Dependency injection
		self.formatter = formatter
	
	def get_book(self, book: Book):
		return self.formatter.format(book)


formatters = Formatter()
p = Printer(formatters)
fancy_formatter = FancyFlyer()
p2 = Printer(fancy_formatter)
boook = Book("Content", "Title", "Author")
print()
print(p.get_book(boook))
print()
print()
print(p2.get_book(boook))
