from project.baked_food.baked_food import BakedFood


class Cake(BakedFood):
	PORTION_SIZE = 245
	
	def __init__(self, name, price: float):
		super().__init__(name, Cake.PORTION_SIZE, price)
	