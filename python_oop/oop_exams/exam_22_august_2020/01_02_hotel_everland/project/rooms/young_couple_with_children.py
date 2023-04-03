from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
	@property
	def count_of_people(self):
		return 2
	
	def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
		super().__init__(family_name, salary_two + salary_one, self.count_of_people + len(children))
		self.room_cost = 30
		self.appliances = []
		self.children = list(children)
		
		for person in range(self.count_of_people + len(children)):
			self.appliances.append(TV())
			self.appliances.append(Fridge())
			self.appliances.append(Laptop())
		
		self.calculate_expenses(*self.appliances + self.children)


