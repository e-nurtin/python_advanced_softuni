from project.hardware.hardware import Hardware
from math import floor


class PowerHardware(Hardware):
	@property
	def type_of_hardware(self):
		return "Power"
	
	def __init__(self, name: str, capacity: int, memory: int):
		super().__init__(name, self.type_of_hardware, floor(capacity * 0.25), floor(memory * 1.75))