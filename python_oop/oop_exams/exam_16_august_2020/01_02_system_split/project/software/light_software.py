from project.software.software import Software
from math import floor


class LightSoftware(Software):
	@property
	def type_of_software(self):
		return "Light"
	
	def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
		super().__init__(name, self.type_of_software, floor(capacity_consumption * 1.5), floor(memory_consumption * 0.5))
