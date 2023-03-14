from typing import List
from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.horse import Horse
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
	VALID_HORSE_TYPES = {"Appaloosa": Appaloosa, "Thoroughbred": Thoroughbred}
	
	def __init__(self):
		self.horses: List[Horse] = []
		self.jockeys: List[Jockey] = []
		self.horse_races: List[HorseRace] = []
	
	@staticmethod
	def __find_entity_from_name(entities, name: str):
		for entity in entities:
			if entity.name == name:
				return entity
	
	def __find_horse_race_from_type(self, race_type: str):
		for horse_race in self.horse_races:
			if horse_race.race_type == race_type:
				return horse_race
			
	def __find_horse_from_type(self, horse_type):
		for horse in self.horses[::-1]:
			if horse.__class__.__name__ == horse_type and not horse.is_taken:
				return horse
	
	def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
		if self.__find_entity_from_name(self.horses, horse_name):
			raise Exception(f"Horse {horse_name} has been already added!")
		
		if horse_type in HorseRaceApp.VALID_HORSE_TYPES:
			
			horse = HorseRaceApp.VALID_HORSE_TYPES[horse_type](horse_name, horse_speed)
			self.horses.append(horse)
			
			return f"{horse_type} horse {horse_name} is added."
		
	def add_jockey(self, jockey_name: str, age: int):
		if self.__find_entity_from_name(self.jockeys, jockey_name):
			raise Exception(f"Jockey {jockey_name} has been already added!")
		
		jockey = Jockey(jockey_name, age)
		self.jockeys.append(jockey)
		
		return f"Jockey {jockey_name} is added."
	
	def create_horse_race(self, race_type: str):
		if self.__find_horse_race_from_type(race_type):
			raise Exception(f"Race {race_type} has been already created!")
		
		race = HorseRace(race_type)
		self.horse_races.append(race)
		
		return f"Race {race_type} is created."
	
	def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
		jockey = self.__find_entity_from_name(self.jockeys, jockey_name)
		horse = self.__find_horse_from_type(horse_type)
		
		if jockey is None:
			raise Exception(f"Jockey {jockey_name} could not be found!")
		
		elif horse is None:
			raise Exception(f"Horse breed {horse_type} could not be found!")
		
		elif jockey.horse is not None:
			return f"Jockey {jockey_name} already has a horse."
		
		jockey.horse = horse
		horse.is_taken = True
		
		return f"Jockey {jockey_name} will ride the horse {horse.name}."
	
	def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
		horse_race = self.__find_horse_race_from_type(race_type)
		jockey = self.__find_entity_from_name(self.jockeys, jockey_name)
		
		if horse_race is None:
			raise Exception(f"Race {race_type} could not be found!")
		
		elif jockey is None:
			raise Exception(f"Jockey {jockey_name} could not be found!")
		
		elif jockey.horse is None:
			raise Exception(f"Jockey {jockey_name} cannot race without a horse!")
		
		elif jockey in horse_race.jockeys:
			return f"Jockey {jockey_name} has been already added to the {race_type} race."
		
		horse_race.jockeys.append(jockey)
		return f"Jockey {jockey_name} added to the {race_type} race."
	
	def start_horse_race(self, race_type: str):
		horse_race = self.__find_horse_race_from_type(race_type)
		
		if horse_race is None:
			raise Exception(f"Race {race_type} could not be found!")

		elif not len(horse_race.jockeys) > 1:
			raise Exception(f"Horse race {race_type} needs at least two participants!")
		
		winner = sorted(horse_race.jockeys, key=lambda jokey: -jokey.horse.speed)[0]
		
		return f"The winner of the {race_type} race, " \
			f"with a speed of {winner.horse.speed}km/h is {winner.name}!" \
			f" Winner's horse: {winner.horse.name}."
	