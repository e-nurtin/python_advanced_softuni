from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCouple(Room):
	@property
	def count_of_people(self):
		return 2
	
	def __init__(self, family_name: str, salary_one: float, salary_two: float):
		super().__init__(family_name, salary_one + salary_two, self.count_of_people)
		self.room_cost = 20
		self.appliances = []
		
		for person in range(self.count_of_people):
			self.appliances.append(TV())
			self.appliances.append(Fridge())
			self.appliances.append(Laptop())
		
		self.calculate_expenses(*self.appliances)
		

