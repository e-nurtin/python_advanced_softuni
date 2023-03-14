from typing import List
from project.meals.meal import Meal


class Client:
	def __init__(self, phone_number: str):
		self.phone_number = phone_number
		self.shopping_cart: List[Meal] = []
		self.bill = 0.0
		self.meal_quantities = {}
	
	@property
	def phone_number(self):
		return self._phone_number
	
	@phone_number.setter
	def phone_number(self, value):
		starts_with_0 = value.startswith('0')
		ten_chars = len(value) == 10
		contains_only_digits = all(char.isdigit() for char in value)
		
		if not all([starts_with_0, ten_chars, contains_only_digits]):
			raise ValueError("Invalid phone number!")
		
		self._phone_number = value
	
	def process_order(self, meal: Meal, meal_name, quantity):
		self.meal_quantities[meal_name] = self.meal_quantities.get(meal_name, 0) + quantity
		self.bill += meal.price * quantity
		self.shopping_cart.append(meal)
	
	def all_meals(self):
		return ', '.join([meal.name for meal in self.shopping_cart])
	
	def reset_cart_and_bill(self):
		self.meal_quantities = {}
		self.shopping_cart = []
		self.bill = 0
