from abc import ABC, abstractmethod


class Booth(ABC):
	PRICE_PER_PERSON = 0
	
	@abstractmethod
	def __init__(self, booth_number: int, capacity: int):
		self.booth_number = booth_number
		self.capacity = capacity
		self.delicacy_orders = []
		self.price_for_reservation: float = 0
		self.is_reserved: bool = False
	
	@property
	def capacity(self):
		return self._capacity
	
	@capacity.setter
	def capacity(self, value):
		if value < 0:
			raise ValueError("Capacity cannot be a negative number!")
		self._capacity = value
	
	def reserve(self, number_of_people):
		self.price_for_reservation = self.PRICE_PER_PERSON * number_of_people
		self.is_reserved = True
	
	def order_delicacy(self, delicacy_order):
		self.delicacy_orders.append(delicacy_order)
	
	def calculate_bill(self):
		bill = self.price_for_reservation + sum([delicacy.price for delicacy in self.delicacy_orders])
		return bill
	
	def free_booth(self):
		self.delicacy_orders = []
		self.price_for_reservation = 0
		self.is_reserved = False
