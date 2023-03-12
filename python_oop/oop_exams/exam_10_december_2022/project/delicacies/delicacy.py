from abc import ABC, abstractmethod


class Delicacy(ABC):
	@abstractmethod
	def __init__(self, name: str, price: float):
		self.name = name
		self.price = price
		self.portion = 0
		
	def details(self):
		return f"{self.__class__.__name__} {self.name}: {self.portion}g - {self.price:.2f}lv."
	