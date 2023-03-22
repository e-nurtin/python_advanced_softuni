from abc import ABC, abstractmethod


class Astronaut(ABC):
	@abstractmethod
	def __init__(self, name: str, oxygen: int):
		self.name = name
		self.oxygen = oxygen
		self.backpack = []
	
	@property
	def breath_units(self):
		return 10
	
	@property
	def name(self):
		return self.__name
	
	@name.setter
	def name(self, value):
		if value.strip() == "":
			raise ValueError("Astronaut name cannot be empty string or whitespace!")
		self.__name = value
	
	def breathe(self):
		self.oxygen -= self.breath_units
	
	def increase_oxygen(self, amount: int):
		self.oxygen += amount
	
	def details(self):
		return f"Name: {self.name}\nOxygen: {self.oxygen}" \
			f"\nBackpack items: {', '.join(self.backpack) if self.backpack else 'none'}"
