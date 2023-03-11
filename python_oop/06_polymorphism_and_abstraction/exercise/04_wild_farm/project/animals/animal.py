from abc import ABC, abstractmethod


class Animal(ABC):
	@abstractmethod
	def __init__(self, name: str, weight: float):
		self.name = name
		self.weight = weight
		self.food_eaten = 0
	

class Bird(Animal):
	def __init__(self, name: str, weight: float, wing_size: float):
		super().__init__(name, weight)
		self.wing_size = wing_size
		
	def __repr__(self):
		return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal):
	def __init__(self, name: str, weight: float, living_region: str):
		super().__init__(name, weight)
		self.living_region = living_region
	
	def __repr__(self):
		return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"
