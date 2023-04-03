from project.appliances.tv import TV
from project.rooms.room import Room


class AloneYoung(Room):
	@property
	def count_of_people(self):
		return 1
	
	def __init__(self, family_name: str, salary: float):
		super().__init__(family_name, salary, self.count_of_people)
		self.room_cost = 10
		self.appliances = [TV()]
		self.calculate_expenses(*self.appliances)
		
	
