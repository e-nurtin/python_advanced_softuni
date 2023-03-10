from abc import ABC, abstractmethod


class Delicacy(ABC):
	@abstractmethod
	def __init__(self, name: str, price: float):
		self.name = name
		self.price = price
		self.portion = 0
	
	@property
	def name(self):
		return self._name
	
	@name.setter
	def name(self, value):
		if value.strip() == "":
			raise ValueError("Name cannot be null or whitespace!")
		self._name = value
	
	@property
	def price(self):
		return self._price
	
	@price.setter
	def price(self, value):
		if value <= 0:
			raise ValueError("Price cannot be less or equal to zero!")
		self._price = value
	
	def details(self):
		return f"{self.__class__.__name__} {self.name}: {self.portion}g - {self.price:.2f}lv."
