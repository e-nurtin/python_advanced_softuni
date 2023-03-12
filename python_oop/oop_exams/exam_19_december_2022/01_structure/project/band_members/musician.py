from abc import ABC, abstractmethod


class Musician(ABC):
	AVAILABLE_SKILLS = []
	
	@abstractmethod
	def __init__(self, name: str, age: int):
		self.name = name
		self.age = age
		self.skills = []
	
	@property
	def name(self):
		return self._name
	
	@name.setter
	def name(self, value):
		if value.strip() == "":
			raise ValueError("Musician name cannot be empty!")
		self._name = value
	
	@property
	def age(self):
		return self._age
	
	@age.setter
	def age(self, value):
		if value < 16:
			raise ValueError("Musicians should be at least 16 years old!")
		self._age = value
	
	def learn_new_skill(self, new_skill: str):
		if new_skill not in self.AVAILABLE_SKILLS:
			raise ValueError(f"{new_skill} is not a needed skill!")
		
		elif new_skill in self.skills:
			raise Exception(f"{new_skill} is already learned!")
		
		self.skills.append(new_skill)
		return f"{self.name} learned to {new_skill}."
	
	@classmethod
	def from_name(cls, name: str, age: int):
		return cls(name, age)