from abc import ABC, abstractmethod


class Meal(ABC):
	@abstractmethod
	def __init__(self, name: str, price: float, quantity: int):
		self.name = name
		self.price = price
		self.quantity = quantity
	
	@property
	def name(self):
		return self._name
	
	@name.setter
	def name(self, value):
		if value == "":
			raise ValueError("Name cannot be an empty string!")
		self._name = value
	
	@property
	def price(self):
		return self._price
	
	@price.setter
	def price(self, value):
		if value <= 0:
			raise ValueError("Invalid price!")
		self._price = value
	
	@abstractmethod
	def details(self):
		pass
	
	