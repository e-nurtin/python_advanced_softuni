from typing import List, Dict
from project.client import Client
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.meal import Meal
from project.meals.starter import Starter


class FoodOrdersApp:
	RECEIPT_ID = 1
	AVAILABLE_MEALS: Dict[str, Meal] = {'Starter': Starter, 'MainDish': MainDish, 'Dessert': Dessert}
	
	def __init__(self):
		self.menu: List[Meal] = []
		self.clients_list: List[Client] = []
	
	@property
	def receipt_id(self) -> int:
		result = FoodOrdersApp.RECEIPT_ID
		FoodOrdersApp.RECEIPT_ID += 1
		return result
	
	@staticmethod
	def __find_client_by_phone_number(clients: List[Client], phone_number: str):
		for client in clients:
			if client.phone_number == phone_number:
				return client
		return None
	
	@staticmethod
	def __is_menu_ready(menu):
		if len(menu) < 5:
			return False
		return True
	
	@staticmethod
	def __find_meal_by_name(meals, meal_name):
		for meal in meals:
			if meal.name == meal_name:
				return meal
		return
	
	def __update_menu_quantities(self, clients_shopping_cart, clients_quantities):
		for meal in clients_shopping_cart:
			menu_meal = FoodOrdersApp.__find_meal_by_name(self.menu, meal.name)
			menu_meal.quantity += clients_quantities[meal.name]
	
	def __check_meals_and_quantities(self, meal_names_and_quantities):
		for meal_name, quantity in meal_names_and_quantities.items():
			meal = self.__find_meal_by_name(self.menu, meal_name)
			
			if meal is None:
				raise Exception(f"{meal_name} is not on the menu!")
			
			elif meal.quantity < quantity:
				raise Exception(f"Not enough quantity of {meal.__class__.__name__}: {meal_name}!")
		
		return True
	
	def register_client(self, client_phone_number: str):
		if self.__find_client_by_phone_number(self.clients_list, client_phone_number):
			raise Exception("The client has already been registered!")
		
		self.clients_list.append(Client(client_phone_number))
		return f"Client {client_phone_number} registered successfully."
	
	def add_meals_to_menu(self, *meals: Meal):
		for meal in meals:
			if meal.__class__.__name__ in FoodOrdersApp.AVAILABLE_MEALS:
				self.menu.append(meal)
	
	def show_menu(self):
		if not self.__is_menu_ready(self.menu):
			raise Exception("The menu is not ready!")
		
		return '\n'.join([meal.details() for meal in self.menu])
	
	def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
		self.show_menu()
		client = self.__find_client_by_phone_number(self.clients_list, client_phone_number)
		
		if not client:
			self.register_client(client_phone_number)
			client = self.__find_client_by_phone_number(self.clients_list, client_phone_number)
		
		if self.__check_meals_and_quantities(meal_names_and_quantities):
			
			for meal_name, quantity in meal_names_and_quantities.items():
				meal = self.__find_meal_by_name(self.menu, meal_name)
				meal.quantity -= quantity
				
				client.process_order(meal, meal_name, quantity)
			
			return f"Client {client.phone_number} successfully ordered {client.all_meals()} for {client.bill:.2f}lv."
	
	def cancel_order(self, client_phone_number: str):
		client = self.__find_client_by_phone_number(self.clients_list, client_phone_number)
		
		if len(client.shopping_cart) == 0:
			raise Exception("There are no ordered meals!")
		
		self.__update_menu_quantities(client.shopping_cart, client.meal_quantities)
		client.reset_cart_and_bill()
		
		return f"Client {client.phone_number} successfully canceled his order."
	
	def finish_order(self, client_phone_number: str):
		client = self.__find_client_by_phone_number(self.clients_list, client_phone_number)
		
		if len(client.shopping_cart) == 0:
			raise Exception("There are no ordered meals!")
		
		result = f"Receipt #{self.receipt_id} with total amount of {client.bill:.2f} was successfully paid for {client.phone_number}."
		client.reset_cart_and_bill()
		
		return result
	
	def __str__(self):
		return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."
