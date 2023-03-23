from abc import ABC, abstractmethod
from math import log2


class Computer(ABC):
	def __init__(self, manufacturer: str, model: str):
		self.manufacturer = manufacturer
		self.model = model
		self.processor = None
		self.ram = None
		self.price = 0
	
	@property
	@abstractmethod
	def computer_type(self):
		...
	
	@property
	@abstractmethod
	def available_processors(self):
		...
	
	@property
	@abstractmethod
	def max_ram(self):
		...
	
	@property
	def manufacturer(self):
		return self.__manufacturer
	
	@manufacturer.setter
	def manufacturer(self, value):
		if value.strip() == "":
			raise ValueError("Manufacturer name cannot be empty.")
		self.__manufacturer = value
	
	@property
	def model(self):
		return self.__model
	
	@model.setter
	def model(self, value):
		if value.strip() == "":
			raise ValueError("Model name cannot be empty.")
		self.__model = value
	
	def configure_computer(self, processor: str, ram: int):
		if processor not in self.available_processors:
			raise ValueError(
				f"{processor} is not compatible with {self.computer_type} {self.manufacturer} {self.model}!")
		
		if not self.__check_for_valid_ram(ram) or ram > self.max_ram:
			raise ValueError(f"{ram}GB RAM is not compatible with {self.computer_type} {self.manufacturer} {self.model}!")
		
		self.__assemble_computer(processor, ram)
		return f"Created {self.manufacturer} {self.model} with {processor} and {ram}GB RAM for {self.price}$."
	
	@staticmethod
	def __check_for_valid_ram(ram):
		return str(log2(ram)).endswith('.0')
	
	def __assemble_computer(self, processor, ram_gb):
		price_for_level_of_ram = 100
		self.ram = ram_gb
		self.processor = processor
		self.price = self.available_processors[processor] + int(log2(ram_gb)) * price_for_level_of_ram
	
	def __repr__(self):
		return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"
