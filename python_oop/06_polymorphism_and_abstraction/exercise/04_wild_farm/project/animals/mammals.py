from project import Mammal
from project import MakeSound, FeedAnimal


class Mouse(Mammal, MakeSound, FeedAnimal):
	SOUND = "Squeak"
	WEIGHT_INCREASE = 0.10
	FOOD = ["Fruit", "Vegetable"]
	
	def __init__(self, name: str, weight: float, living_region: str):
		super().__init__(name, weight, living_region)


class Dog(Mammal, MakeSound, FeedAnimal):
	SOUND = "Woof!"
	WEIGHT_INCREASE = 0.4
	FOOD = ["Meat"]
	
	def __init__(self, name: str, weight: float, living_region: str):
		super().__init__(name, weight, living_region)


class Cat(Mammal, MakeSound, FeedAnimal):
	SOUND = "Meow"
	WEIGHT_INCREASE = 0.30
	FOOD = ["Meat", "Vegetable"]
	
	def __init__(self, name: str, weight: float, living_region: str):
		super().__init__(name, weight, living_region)


class Tiger(Mammal, MakeSound, FeedAnimal):
	SOUND = "ROAR!!!"
	WEIGHT_INCREASE = 1
	FOOD = ["Meat"]
	
	def __init__(self, name: str, weight: float, living_region: str):
		super().__init__(name, weight, living_region)
	
