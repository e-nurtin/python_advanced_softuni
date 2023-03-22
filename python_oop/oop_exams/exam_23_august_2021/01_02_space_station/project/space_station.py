from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
	def __init__(self):
		self.planet_repository = PlanetRepository()
		self.astronaut_repository = AstronautRepository()
		self.completed_missions = 0
		self.failed_missions = 0
	
	@property
	def astronaut_types(self):
		return {"Biologist": Biologist, "Geodesist": Geodesist, "Meteorologist": Meteorologist}
	
	def add_astronaut(self, astronaut_type: str, name: str):
		if astronaut_type not in self.astronaut_types:
			raise Exception("Astronaut type is not valid!")
		
		astronaut = self.astronaut_types[astronaut_type](name)
		self.astronaut_repository.add(astronaut)
		return f"Successfully added {astronaut_type}: {name}."
	
	def add_planet(self, name: str, items: str):
		if self.planet_repository.find_by_name(name):
			return f"{name} is already added."
		
		planet = Planet(name, *items.split(', '))
		self.planet_repository.add(planet)
		return f"Successfully added Planet: {name}."
	
	def retire_astronaut(self, name: str):
		astronaut = self.astronaut_repository.find_by_name(name)
		self.astronaut_repository.remove(astronaut)
		return f"Astronaut {name} was retired!"
	
	def recharge_oxygen(self):
		self.astronaut_repository.recharge_oxygen()
	
	def send_on_mission(self, planet_name: str):
		planet = self.planet_repository.find_by_name(planet_name)
		
		if not planet:
			raise Exception("Invalid planet name!")
		
		astronauts = [astro for astro in self.astronaut_repository if astro.oxygen > 30]
		astronauts = list(sorted(astronauts, key=lambda a: -a.oxygen))[:5]
		
		if not astronauts:
			raise Exception("You need at least one astronaut to explore the planet!")
		
		return self.__start_mission(planet, *astronauts)
	
	def __start_mission(self, planet, *astronauts):
		mission_accomplished = False
		
		for count_of_astronauts, astronaut in enumerate(astronauts, 1):
			
			while astronaut.oxygen >= astronaut.breath_units:
				try:
					astronaut.backpack.append(planet.items.pop())
					astronaut.breathe()
					
				except IndexError:
					mission_accomplished = True
					self.completed_missions += 1
					return self.mission_outcome(planet, mission_accomplished, count_of_astronauts)
		
		if len(planet.items) == 0:
			mission_accomplished = True
			
		return self.mission_outcome(planet, mission_accomplished)
	
	@staticmethod
	def mission_outcome(planet, mission_accomplished, *args):
		if mission_accomplished:
			return f"Planet: {planet.name} was explored. {args[0]} astronauts participated in collecting items."
		return "Mission is not completed."

	def report(self):
		result = [
			f"{self.completed_missions} successful missions!",
			f"{self.failed_missions} missions were not completed!",
			f"Astronauts' info:",
		]
		for astronaut in self.astronaut_repository:
			result.append(astronaut.details())
			
		return '\n'.join(result)