from typing import List
from project.astronaut.astronaut import Astronaut


class AstronautRepository:
	def __init__(self):
		self.astronauts: List[Astronaut] = []
		self.index = -1
	
	def __iter__(self):
		return self
	
	def __next__(self):
		if self.index >= len(self.astronauts) - 1:
			self.index = -1
			raise StopIteration
		
		self.index += 1
		return self.astronauts[self.index]
	
	def add(self, astronaut: Astronaut):
		self.astronauts.append(astronaut)
	
	def remove(self, astronaut: Astronaut):
		self.astronauts.remove(astronaut)
	
	def find_by_name(self, name: str):
		for astronaut in self.astronauts:
			if astronaut.name == name:
				return astronaut
			
		raise Exception(f"Astronaut {name} doesn't exist!")
	
	def recharge_oxygen(self):
		for astronaut in self.astronauts:
			astronaut.increase_oxygen(10)