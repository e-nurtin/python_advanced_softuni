from project.room import Room


class Hotel:
	def __init__(self, name: str):
		self.name = name
		self.rooms = []
		self.guests = 0
	
	def show_status(self):
		guest_count, free_rooms, taken_rooms = 0, [], []
		for room in self.rooms:
			if room.is_taken:
				taken_rooms.append(room.number)
			else:
				free_rooms.append(room.number)
		
		return f"Hotel {self.name} has {self.guests} total guests\n" + f"Free rooms: {', '.join(map(str, free_rooms))}\n" + f"Free rooms: {', '.join(map(str, taken_rooms))}"
	
	@classmethod
	def from_stars(cls, stars_count: int) -> 'Hotel':
		return cls(f"{stars_count} stars Hotel")
		
	def add_room(self, room: Room):
		self.rooms.append(room)
	
	def take_room(self, room_number: int, people: int):
		for room in self.rooms:
			if room.number == room_number:
				if room.take_room(people) is None:
					self.guests += room.guests
	
	def free_room(self, room_number: int):
		for room in self.rooms:
			if room.number == room_number:
				guests = room.guests
				if room.free_room() is None:
					self.guests -= guests
				
	def status(self) -> str:
		return self.show_status()