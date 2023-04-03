from typing import List
from project.rooms.room import Room


class Everland:
	def __init__(self):
		self.rooms: List[Room] = []
	
	def add_room(self, room: Room):
		self.rooms.append(room)
	
	def get_monthly_consumptions(self):
		total_consumption = 0
		for room in self.rooms:
			total_consumption += room.room_cost + room.expenses
		return f"Monthly consumptions: {total_consumption:.2f}$."
	
	def pay(self):
		result = []
		for room in self.rooms:
			total_consumption_for_family = room.room_cost + room.expenses
			if room.budget < total_consumption_for_family:
				result.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
				self.rooms.remove(room)
			else:
				room.budget -= total_consumption_for_family
				result.append(
					f"{room.family_name} paid {total_consumption_for_family:.2f}$ and have {room.budget:.2f}$ left.")
		
		return '\n'.join(result)
	
	def status(self):
		result = [f'Total population: {self.__all_people_in_the_hotel()}']
		for room in self.rooms:
			result.append(room.get_status())
			
		return '\n'.join(result)
	
	def __all_people_in_the_hotel(self):
		return sum(r.members_count for r in self.rooms)
