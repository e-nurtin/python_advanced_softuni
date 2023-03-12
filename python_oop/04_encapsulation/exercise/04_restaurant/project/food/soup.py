from project import Starter


class Soup(Starter):
	def __init__(self, name: str, price: float, grams: int):
		super().__init__(name, price, grams)