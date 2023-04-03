from project.appliances.fridge import Fridge
from project.appliances.stove import Stove
from project.appliances.tv import TV
from project.rooms.room import Room


class OldCouple(Room):
	@property
	def count_of_people(self):
		return 2
	
	def __init__(self, family_name: str, pension_one: float, pension_two: float):
		super().__init__(family_name, pension_two + pension_one, self.count_of_people)
		self.room_cost = 15
		self.appliances = []
		
		for person in range(self.count_of_people):
			self.appliances.append(TV())
			self.appliances.append(Fridge())
			self.appliances.append(Stove())
		
		self.calculate_expenses(*self.appliances)

