from typing import List
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
	def __init__(self):
		self.robots: List[MaleRobot, FemaleRobot] = []
		self.services: List[SecondaryService, MainService] = []
	
	@property
	def valid_service_types(self):
		return {"MainService": MainService, "SecondaryService": SecondaryService}
	
	@property
	def valid_robot_types(self):
		return {"FemaleRobot": FemaleRobot, "MaleRobot": MaleRobot}
	
	@staticmethod
	def __get_entity_from_name(entity_name, entities):
		for entity in entities:
			if entity.name == entity_name:
				return entity
	
	def add_service(self, service_type: str, name: str):
		if service_type not in self.valid_service_types:
			raise Exception("Invalid service type!")
		
		service = self.valid_service_types[service_type](name)
		self.services.append(service)
		
		return f"{service_type} is successfully added."
	
	def add_robot(self, robot_type: str, name: str, kind: str, price: float):
		if robot_type not in self.valid_robot_types:
			raise Exception("Invalid robot type!")
		
		robot = self.valid_robot_types[robot_type](name, kind, price)
		self.robots.append(robot)
		
		return f"{robot_type} is successfully added."
	
	def add_robot_to_service(self, robot_name: str, service_name: str):
		robot = self.__get_entity_from_name(robot_name, self.robots)
		service = self.__get_entity_from_name(service_name, self.services)
		
		if robot.service_type != service.service_type:
			return "Unsuitable service."
		
		elif not service.has_capacity_for_robot():
			return "Not enough capacity for this robot!"
		
		self.robots.remove(robot)
		service.robots.append(robot)
		
		return f"Successfully added {robot_name} to {service_name}."
	
	def remove_robot_from_service(self, robot_name: str, service_name: str):
		service = self.__get_entity_from_name(service_name, self.services)
		robot = self.__get_entity_from_name(robot_name, service.robots)
		
		if robot is None:
			raise Exception("No such robot in this service!")
		
		service.robots.remove(robot)
		self.robots.append(robot)
		
		return f"Successfully removed {robot_name} from {service_name}."
	
	def feed_all_robots_from_service(self, service_name: str):
		service = self.__get_entity_from_name(service_name, self.services)
		
		count_of_robots = service.feed_all_robots()
		return f"Robots fed: {count_of_robots}."
	
	def service_price(self, service_name: str):
		service = self.__get_entity_from_name(service_name, self.services)
		
		return f"The value of service {service_name} is {service.price_of_all_robots:.2f}."
	
	def __str__(self):
		result = []
		
		for service in self.services:
			result.append(service.details())
		
		return '\n'.join(result)
