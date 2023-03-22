from typing import List
from project.planet.planet import Planet


class PlanetRepository:
	def __init__(self):
		self.planets: List[Planet] = []
		self.index = -1
		
	def __iter__(self):
		return self
	
	def __next__(self):
		if self.index >= len(self.planets) - 1:
			self.index = - 1
			raise StopIteration
		
		self.index += 1
		return self.planets[self.index]
	
	def add(self, planet: Planet):
		self.planets.append(planet)
		
	def remove(self, planet: Planet):
		self.planets.remove(planet)
	
	def find_by_name(self, name: str):
		for planet in self.planets:
			if planet.name == name:
				return planet