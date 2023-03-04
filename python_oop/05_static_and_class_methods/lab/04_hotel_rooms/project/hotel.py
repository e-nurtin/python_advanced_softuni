from project.room import Room


class Hotel:
	def __init__(self, name: str):
		self.name = name
		self.rooms = []
	
	def show_status(self):
		free_rooms, taken_rooms = [], []
		for room in self.rooms:
			if room.is_taken:
				taken_rooms.append(room.number)
			else:
				free_rooms.append(room.number)
		
		return f"Hotel {self.name} has {self.guests} total guests\n" +\
			f"Free rooms: {', '.join(map(str, free_rooms))}\n" +\
			f"Taken rooms: {', '.join(map(str, taken_rooms))}"
	
	@property
	def guests(self):
		return sum([r.guests for r in self.rooms])
	
	@classmethod
	def from_stars(cls, stars_count: int) -> 'Hotel':
		return cls(f"{stars_count} stars Hotel")
	
	def add_room(self, room: Room):
		self.rooms.append(room)
	
	def take_room(self, room_number: int, people: int):
		for room in self.rooms:
			if room.number == room_number:
				return room.take_room(people)
	
	def free_room(self, room_number: int):
		for room in self.rooms:
			if room.number == room_number:
				return room.free_room()
	
	def status(self) -> str:
		return self.show_status()
