from project.animals.animal import Bird
from project.animals.mixins import MakeSound, FeedAnimal


class Owl(Bird, MakeSound, FeedAnimal):
	SOUND = "Hoot Hoot"
	WEIGHT_INCREASE = 0.25
	FOOD = ["Meat"]
	
	def __init__(self, name: str, weight: float, wing_size: float):
		super().__init__(name, weight, wing_size)


class Hen(Bird, MakeSound, FeedAnimal):
	SOUND = "Cluck"
	WEIGHT_INCREASE = 0.35
	FOOD = ["Meat", "Vegetable", "Fruit", "Seed"]
	
	def __init__(self, name: str, weight: float, wing_size: float):
		super().__init__(name, weight, wing_size)
