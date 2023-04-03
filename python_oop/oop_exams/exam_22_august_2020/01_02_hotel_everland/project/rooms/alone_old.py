from project.rooms.room import Room


class AloneOld(Room):
	@property
	def count_of_people(self):
		return 1
	
	def __init__(self, family_name: str, pension: float):
		super().__init__(family_name, pension, self.count_of_people)
		self.room_cost = 10