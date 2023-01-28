class PizzaDelivery:
	def __init__(self, name, price, ingredients: dict):
		self.name = name
		self.price = price
		self.ingredients = ingredients
		self.ordered = False
	
	def add_extra(self, ingredient: str, quantity: int, price_per_quantity: float):
		if not self.ordered:
			if not ingredient in self.ingredients:
				self.ingredients[ingredient] = 0
			
			self.ingredients[ingredient] += quantity
			self.price += price_per_quantity * quantity
		return f"Pizza {self.name} already prepared, and we can't make any changes!"
	
	def remove_ingredient(self, ingredient: str, quantity: int, price_per_quantity: float):
		if not self.ordered:
			if ingredient in self.ingredients:
				
				if quantity > self.ingredients[ingredient]:
					return f"Please check again the desired quantity of {ingredient}!"
				
				self.ingredients[ingredient] -= quantity
				self.price -= price_per_quantity * quantity
			
			return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
		return f"Pizza {self.name} already prepared, and we can't make any changes!"
	
	def make_order(self):
		self.ordered = True
		ingredients = ', '.join([f'{k}: {v}' for k, v in self.ingredients.items()])
		
		return f"You've ordered pizza {self.name} prepared with " \
		       f"{ingredients} and the price will be {self.price}lv."
