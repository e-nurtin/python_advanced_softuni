from abc import ABC, abstractmethod


class Animal(ABC):  # We created a blueprint for all the Animals that we will create. They all make a sound
	@abstractmethod
	def make_sound(self):
		pass


class Cat(Animal):
	def make_sound(self):
		return "meow"


class Dog(Animal):
	def make_sound(self):
		return 'woof-woof'


class Chicken(Animal):
	def make_sound(self):
		return 'wak'


def animal_sound(animals: list):
	for animal in animals:
		print(f"{animal.__class__.__name__} says {animal.make_sound()}")


animals = [Cat(), Dog(), Chicken()]
animal_sound(animals)
