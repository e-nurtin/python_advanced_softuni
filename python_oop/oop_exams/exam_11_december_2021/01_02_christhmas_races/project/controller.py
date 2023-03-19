from typing import List

from project.car.car import Car
from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
	def __init__(self):
		self.cars: List[Car] = []
		self.drivers: List[Driver] = []
		self.races: List[Race] = []
	
	@property
	def valid_car_types(self):
		return {"MuscleCar": MuscleCar, "SportsCar": SportsCar}
	
	def create_car(self, car_type: str, model: str, speed_limit: int):
		if car_type not in self.valid_car_types:
			return
		
		if self.__get_car_with_same_model(model):
			raise Exception(f"Car {model} is already created!")
		
		self.cars.append(self.valid_car_types[car_type](model, speed_limit))
		return f"{car_type} {model} is created."
	
	def __get_car_with_same_model(self, model):
		for car in self.cars:
			if car.model == model:
				return car
	
	def create_driver(self, driver_name: str):
		if self.__get_entity_from_name(self.drivers, driver_name):
			raise Exception(f"Driver {driver_name} is already created!")
		
		self.drivers.append(Driver(driver_name))
		return f"Driver {driver_name} is created."
	
	@staticmethod
	def __get_entity_from_name(entities, entity_name):
		for entity in entities:
			if entity.name == entity_name:
				return entity
	
	def create_race(self, race_name: str):
		if self.__get_entity_from_name(self.races, race_name):
			raise Exception(f"Race {race_name} is already created!")
		
		self.races.append(Race(race_name))
		return f"Race {race_name} is created."
	
	def add_car_to_driver(self, driver_name: str, car_type: str):
		driver = self.__get_entity_from_name(self.drivers, driver_name)
		car = self.__get_car_from_type(car_type)
		if not driver:
			raise Exception(f"Driver {driver_name} could not be found!")
		
		elif not car:
			raise Exception(f"Car {car_type} could not be found!")
		
		elif driver.car is not None:
			old_model = driver.car.model
			driver.car.is_taken = False
			driver.car = car
			car.is_taken = True
			return f"Driver {driver_name} changed his car from {old_model} to {car.model}."
		
		driver.car = car
		return f"Driver {driver_name} chose the car {car.model}."
	
	def __get_car_from_type(self, car_type):
		if car_type not in self.valid_car_types:
			return
		
		for car in self.cars[::-1]:
			if type(car).__name__ == car_type and not car.is_taken:
				return car
	
	def add_driver_to_race(self, race_name: str, driver_name: str):
		driver = self.__get_entity_from_name(self.drivers, driver_name)
		race = self.__get_entity_from_name(self.races, race_name)
		
		if not race:
			raise Exception(f"Race {race_name} could not be found!")
		
		elif not driver:
			raise Exception(f"Driver {driver_name} could not be found!")
		
		elif driver.car is None:
			raise Exception(f"Driver {driver_name} could not participate in the race!")
		
		elif driver in race.drivers:
			return f"Driver {driver_name} is already added in {race_name} race."
		
		race.drivers.append(driver)
		return f"Driver {driver_name} added in {race_name} race."
	
	def start_race(self, race_name: str):
		race = self.__get_entity_from_name(self.races, race_name)
		
		if not race:
			raise Exception(f"Race {race_name} could not be found!")
		
		elif len(race.drivers) < 3:
			raise Exception(f"Race {race_name} cannot start with less than 3 participants!")
		
		result = []
		for driver in list(sorted(race.drivers, key=lambda x: -x.car.speed_limit))[:3]:
			driver.number_of_wins += 1
			result.append(f"Driver {driver.name} wins the {race_name} race with a speed of {driver.car.speed_limit}.")
		
		return '\n'.join(result)
