from typing import List

from project.computer_types.computer import Computer


class ComputerStoreApp:
	def __init__(self):
		self.warehouse: List[Computer] = []
		self.profits = 0
	
	def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
		pass
	
	def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
		pass
	
