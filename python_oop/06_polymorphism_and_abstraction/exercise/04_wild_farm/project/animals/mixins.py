class MakeSound:
	SOUND = ''
	
	@classmethod
	def make_sound(cls):
		return cls.SOUND


class FeedAnimal:
	FOOD = ''
	WEIGHT_INCREASE = 0
	
	def __init__(self):
		self.food_eaten = None
		self.weight = None
	
	def feed(self, food):
		if food.__class__.__name__ not in self.FOOD:
			return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
		
		self.weight += (self.WEIGHT_INCREASE * food.quantity)
		self.food_eaten += food.quantity