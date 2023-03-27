from project.baked_food.baked_food import BakedFood


class Bread(BakedFood):
	PORTION_SIZE = 200
	
	def __init__(self, name, price: float):
		super().__init__(name, Bread.PORTION_SIZE, price)
