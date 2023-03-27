from typing import List
from project.baked_food.baked_food import BakedFood
from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.drink import Drink
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable
from project.table.table import Table


class Bakery:
	def __init__(self, name: str):
		self.name = name
		self.food_menu: List[BakedFood] = []
		self.drinks_menu: List[Drink] = []
		self.tables_repository: List[Table] = []
		self.__total_income = 0
		self.total_income = 0
	
	@property
	def valid_food_types(self):
		return {"Bread": Bread, "Cake": Cake}
	
	@property
	def valid_drink_types(self):
		return {"Tea": Tea, "Water": Water}
	
	@property
	def valid_table_types(self):
		return {"InsideTable": InsideTable, "OutsideTable": OutsideTable}
	
	@property
	def name(self):
		return self.__name
	
	@name.setter
	def name(self, value):
		if value.strip() == '':
			raise ValueError("Name cannot be empty string or white space!")
		self.__name = value
	
	@staticmethod
	def __get_entity_from_name(entities, entity_name):
		for entity in entities:
			if entity.name == entity_name:
				return entity
	
	def __get_table_from_number(self, table_number):
		for table in self.tables_repository:
			if table.table_number == table_number:
				return table
	
	def __process_order(self, table, type_of_order, *order):
		
		items_that_are_not_available = []
		result = [f"Table {table.table_number} ordered:"]
		
		for item_name in order:
			
			if type_of_order == 'food':
				item = self.__get_entity_from_name(self.food_menu, item_name)
			else:
				item = self.__get_entity_from_name(self.drinks_menu, item_name)
			
			if not item:
				items_that_are_not_available.append(item_name)
			
			else:
				
				if type_of_order == 'food':
					table.order_food(item)
				else:
					table.order_drink(item)
				
				result.append(str(item))
		
		result.append(f"{self.name} does not have in the menu:")
		for item in items_that_are_not_available:
			result.append(item)
		
		return '\n'.join(result)
	
	# This is where Judge required methods start
	#
	def add_food(self, food_type: str, name: str, price: float):
		if self.__get_entity_from_name(self.food_menu, name):
			raise Exception(f"{food_type} {name} is already in the menu!")
		
		if food_type not in self.valid_food_types:
			return
		
		food = self.valid_food_types[food_type](name, price)
		self.food_menu.append(food)
		
		return f"Added {name} ({food_type}) to the food menu"
	
	def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
		if self.__get_entity_from_name(self.drinks_menu, name):
			raise Exception(f"{drink_type} {name} is already in the menu!")
		
		if drink_type not in self.valid_drink_types:
			return
		
		drink = self.valid_drink_types[drink_type](name, portion, brand)
		self.drinks_menu.append(drink)
		
		return f"Added {name} ({brand}) to the drink menu"
	
	def add_table(self, table_type: str, table_number: int, capacity: int):
		if self.__get_table_from_number(table_number):
			raise Exception(f"Table {table_number} is already in the bakery!")
		
		if table_type not in self.valid_table_types:
			return
		
		table = self.valid_table_types[table_type](table_number, capacity)
		self.tables_repository.append(table)
		
		return f"Added table number {table_number} in the bakery"
	
	def reserve_table(self, number_of_people: int):
		for table in self.tables_repository:
			
			if table.capacity >= number_of_people and not table.is_reserved:
				table.reserve(number_of_people)
				
				return f"Table {table.table_number} has been reserved for {number_of_people} people"
		
		return f"No available table for {number_of_people} people"
	
	def order_food(self, table_number: int, *food_order):
		table = self.__get_table_from_number(table_number)
		
		if not table:
			return f"Could not find table {table_number}"
		
		return self.__process_order(table, 'food', *food_order)
	
	def order_drink(self, table_number: int, *drinks_order):
		table = self.__get_table_from_number(table_number)
		
		if not table:
			return f"Could not find table {table_number}"
		
		return self.__process_order(table, 'drink', *drinks_order)
	
	def leave_table(self, table_number: int):
		table = self.__get_table_from_number(table_number)
		if table:
			table_bill = table.get_bill()
			self.__total_income += table_bill
			table.clear()
			
			return f"Table: {table_number}\nBill: {table_bill:.2f}"
	
	def get_free_tables_info(self):
		result = []
		for table in self.tables_repository:
			free = table.free_table_info()
			if free:
				result.append(free)
		return '\n'.join(result)
		# return '\n'.join(t.free_table_info() for t in self.tables_repository)
	
	def get_total_income(self):
		return f"Total income: {self.__total_income:.2f}lv"
