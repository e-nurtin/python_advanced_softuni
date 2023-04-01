from project.band_members.musician import Musician
from typing import List


class Band:
	def __init__(self, name: str):
		self.name = name
		self.members: List[Musician] = []
	
	@property
	def name(self):
		return self._name
	
	@name.setter
	def name(self, value):
		if value == "":
			raise ValueError("Band name should contain at least one character!")
		self._name = value
	
	@classmethod
	def from_name(cls, name: str) -> 'Band':
		return cls(name)
	
	def add_member(self, member: Musician):
		self.members.append(member)
	
	def remove_member(self, member: Musician):
		self.members.remove(member)
	
	def __str__(self):
		return f"{self.name} with {len(self.members)} members."
