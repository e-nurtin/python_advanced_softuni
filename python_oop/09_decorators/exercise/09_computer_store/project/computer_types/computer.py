from abc import ABC, abstractmethod


class Computer(ABC):
	def __init__(self, manufacturer: str, model: str):
		self.manufacturer = manufacturer
		self.model = model
		self.processor = None
		self.ram = None
		self.price = 0
	
	@property
	def computer_type(self):
		types = {"Laptop": "Laptop", "DesktopComputer": "Desktop Computer"}
		return types[self.__class__.__name__]
	
	@abstractmethod
	@property
	def available_processors(self):
		pass
	
	@abstractmethod
	@property
	def max_ram(self):
		pass
	
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
		
		level_of_ram = self.__check_for_valid_ram(ram)
		price = self.__assemble_computer(processor, level_of_ram, ram)
		return f"Created {self.manufacturer} {self.model} with {processor} and {ram}GB RAM for {price}$."
	
	def __check_for_valid_ram(self, ram):
		level_of_power_of_two = 1
		current_ram = 2
		
		while current_ram <= self.max_ram:
			level_of_power_of_two += 1
			
			if current_ram == ram:
				return level_of_power_of_two
			
			current_ram = 2 ** level_of_power_of_two
		
		raise ValueError(f"{ram}GB RAM is not compatible with {self.computer_type} {self.manufacturer} {self.model}!")
	
	def __assemble_computer(self, processor, level_of_ram, ram_gb):
		price_for_level_of_ram = 100
		price = 0
		self.ram = ram_gb
		self.processor = processor
		price += self.available_processors[processor] + level_of_ram * price_for_level_of_ram
		return price
