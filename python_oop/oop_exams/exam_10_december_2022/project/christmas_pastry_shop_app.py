from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
	DELICACIES = {'Gingerbread': Gingerbread, 'Stolen': Stolen}
	BOOTHS = {"Open Booth": OpenBooth, "Private Booth": PrivateBooth}
	
	def __init__(self):
		self.booths = []
		self.delicacies = []
		self.income: float = 0.0
	
	@staticmethod
	def __find_entity_from_name(entities_to_check, name_to_search_for):
		for entity in entities_to_check:
			if entity.name == name_to_search_for:
				return entity
		return
	
	@staticmethod
	def __find_booth(booths_to_check, booth_number):
		for booth in booths_to_check:
			if booth.booth_number == booth_number:
				return booth
		return
	
	@staticmethod
	def __check_for_empty_booth(booths, people_to_accommodate):
		for booth in booths:
			if not booth.is_reserved and booth.capacity >= people_to_accommodate:
				return booth
		return
	
	def add_delicacy(self, type_delicacy: str, name: str, price: float):
		if self.__find_entity_from_name(self.delicacies, name):
			raise Exception(f"{name} already exists!")
		
		elif type_delicacy not in ChristmasPastryShopApp.DELICACIES:
			raise Exception(f"{type_delicacy} is not on our delicacy menu!")
		
		self.delicacies.append(ChristmasPastryShopApp.DELICACIES[type_delicacy](name, price))
		return f"Added delicacy {name} - {type_delicacy} to the pastry shop."
	
	def add_booth(self, type_booth: str, booth_number: int, capacity: int):
		if self.__find_booth(self.booths, booth_number):
			raise Exception(f"Booth number {booth_number} already exists!")
		
		elif type_booth not in ChristmasPastryShopApp.BOOTHS:
			raise f"{type_booth} is not a valid booth!"
		
		self.booths.append(ChristmasPastryShopApp.BOOTHS[type_booth](booth_number, capacity))
		return f"Added booth number {booth_number} in the pastry shop."
	
	def reserve_booth(self, number_of_people: int):
		booth = self.__check_for_empty_booth(self.booths, number_of_people)
		if booth is None:
			raise Exception(f"No available booth for {number_of_people} people!")
		
		booth.reserve(number_of_people)
		return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."
	
	def order_delicacy(self, booth_number: int, delicacy_name: str):
		booth = self.__find_booth(self.booths, booth_number)
		delicacy = self.__find_entity_from_name(self.delicacies, delicacy_name)
		
		if booth is None:
			raise Exception(f"Could not find booth {booth_number}!")
		
		elif delicacy is None:
			raise Exception(f"No {delicacy_name} in the pastry shop!")
		
		booth.order_delicacy(delicacy)
		return f"Booth {booth_number} ordered {delicacy_name}."
	
	def leave_booth(self, booth_number: int):
		booth = self.__find_booth(self.booths, booth_number)
		
		bill = booth.calculate_bill()
		booth.free_booth()
		self.income += bill
	
		return f"Booth {booth_number}:\nBill: {bill:.2f}lv."
	
	def get_income(self):
		return f"Income: {self.income:.2f}lv."
	