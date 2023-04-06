from typing import List

from project.software.software import Software


class Hardware:
	def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
		self.name = name
		self.hardware_type = hardware_type
		self.capacity = capacity
		self.memory = memory
		self.software_components: List[Software] = []
	
	@property
	def all_components(self):
		return ', '.join([s.name for s in self.software_components]) if self.software_components else 'None'
	
	@property
	def express_components(self):
		return len([s for s in self.software_components if s.software_type == 'Express'])
	
	@property
	def light_components(self):
		return len([s for s in self.software_components if s.software_type == 'Light'])
	
	@property
	def memory_occupied(self):
		return sum([s.memory_consumption for s in self.software_components])
	
	@property
	def capacity_occupied(self):
		return sum([s.capacity_consumption for s in self.software_components])
	
	def __check_if_available_space_for_software(self, software: Software):
		if self.capacity - self.capacity_occupied < software.capacity_consumption or \
				self.memory - self.memory_occupied < software.memory_consumption:
			raise Exception("Software cannot be installed")
	
	def install(self, software: Software):
		self.__check_if_available_space_for_software(software)
		self.software_components.append(software)
	
	def uninstall(self, software: Software):
		self.software_components.remove(software)
