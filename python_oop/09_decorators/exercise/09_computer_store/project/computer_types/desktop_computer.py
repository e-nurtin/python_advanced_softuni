from project.computer_types.computer import Computer


class DesktopComputer(Computer):
	@property
	def available_processors(self):
		return {"AMD Ryzen 7 5700G": 500, "Intel Core i5-12600K": 600, "Apple M1 Max": 1800}
	
	@property
	def max_ram(self):
		return 128
	
	# def configure_computer(self, processor: str, ram: int):
	# 	if processor not in self.available_processors:
	# 		raise ValueError(f"{ processor } is not compatible with desktop computer {self.manufacturer} {self.model}!")
	#
	# 	level_of_ram = self.__check_for_valid_ram(ram)
	# 	price = self.__assemble_computer(processor, level_of_ram, ram)
	# 	return f"Created {self.manufacturer} {self.model} with {processor} and {ram}GB RAM for {price}$."
	#
	# def __check_for_valid_ram(self, ram):
	# 	level_of_power_of_two = 1
	# 	current_ram = 2
	#
	# 	while current_ram <= self.max_ram:
	# 		level_of_power_of_two += 1
	#
	# 		if current_ram == ram:
	# 			return level_of_power_of_two
	#
	# 		current_ram = 2 ** level_of_power_of_two
	#
	# 	raise ValueError(f"{ram}GB RAM is not compatible with desktop computer {self.manufacturer} {self.model}!")
	#
	# def __assemble_computer(self, processor, level_of_ram, ram_gb):
	# 	price_for_level_of_ram = 100
	# 	price = 0
	# 	self.ram = ram_gb
	# 	self.processor = processor
	# 	price += self.available_processors[processor] + level_of_ram * price_for_level_of_ram
	# 	return price
	#