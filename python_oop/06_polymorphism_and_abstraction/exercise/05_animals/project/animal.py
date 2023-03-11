from abc import ABC, abstractmethod


class Animal(ABC):
	SOUND = ''
	
	@abstractmethod
	def __init__(self, name, age, gender):
		self.name = name
		self.age = age
		self.gender = gender
	
	@classmethod
	def make_sound(cls):
		return cls.SOUND
	
	@abstractmethod
	def __repr__(self):
		pass