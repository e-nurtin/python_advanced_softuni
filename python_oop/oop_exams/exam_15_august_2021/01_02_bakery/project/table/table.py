from abc import ABC, abstractmethod
from typing import List

from project.baked_food.baked_food import BakedFood
from project.drink.drink import Drink


class Table(ABC):
	@abstractmethod
	def __init__(self, table_number: int, capacity: int):
		self.table_number = table_number
		self.capacity = capacity
		
		self.food_orders: List[BakedFood] = []
		self.drink_orders: List[Drink] = []
		self.number_of_people: int = 0
		self.is_reserved: bool = False
	
	@property
	@abstractmethod
	def table_type(self):
		...
	
	def reserve(self, number_of_people: int):
		self.is_reserved = True
		self.number_of_people = number_of_people
		
	def order_food(self, baked_food: BakedFood):
		self.food_orders.append(baked_food)
		
	def order_drink(self, drink: Drink):
		self.drink_orders.append(drink)
		
	def get_bill(self):
		return sum([food.price for food in self.food_orders]) + \
			sum([drink.price for drink in self.drink_orders])
	
	def clear(self):
		self.drink_orders = []
		self.food_orders = []
		self.is_reserved = False
		self.number_of_people = 0
	
	def free_table_info(self):
		if not self.is_reserved:
			return f"Table: {self.table_number}\nType: {self.table_type}\nCapacity: {self.capacity}"
	