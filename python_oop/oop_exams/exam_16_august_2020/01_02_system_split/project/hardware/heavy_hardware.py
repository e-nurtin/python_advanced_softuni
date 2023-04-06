from project.hardware.hardware import Hardware
from math import floor


class HeavyHardware(Hardware):
	@property
	def type_of_hardware(self):
		return "Heavy"
	
	def __init__(self, name: str, capacity: int, memory: int):
		super().__init__(name, self.type_of_hardware, capacity * 2, floor(memory * 0.75))
