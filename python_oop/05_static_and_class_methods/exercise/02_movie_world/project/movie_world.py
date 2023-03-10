from project import Customer
from project import DVD


class MovieWorld:
	def __init__(self, name: str):
		self.name = name
		self.customers = []
		self.dvds = []
	
	@staticmethod
	def dvd_capacity() -> int:
		return 15
	
	@staticmethod
	def customer_capacity() -> int:
		return 10
	
	def add_customer(self, customer: Customer):
		if MovieWorld.customer_capacity() > len(self.customers):
			self.customers.append(customer)

	def add_dvd(self, dvd: DVD):
		if MovieWorld.dvd_capacity() > len(self.dvds):
			self.dvds.append(dvd)
	
	def rent_dvd(self, customer_id: int, dvd_id: int):
		customer = [c for c in self.customers if c.id == customer_id][0]
		dvd = [d for d in self.dvds if d.id == dvd_id][0]
		
		if dvd in customer.rented_dvds:
			return f"{customer.name} has already rented {dvd.name}"
		
		elif dvd.is_rented:
			return "DVD is already rented"
		
		elif dvd.age_restriction > customer.age:
			return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
		
		dvd.is_rented = True
		customer.rented_dvds.append(dvd)
		return f"{customer.name} has successfully rented {dvd.name}"
	
	def return_dvd(self, customer_id: int, dvd_id: int):
		customer = [c for c in self.customers if c.id == customer_id][0]
		dvd = [d for d in self.dvds if d.id == dvd_id][0]
		
		if dvd in customer.rented_dvds:
			dvd.is_rented = False
			customer.rented_dvds.remove(dvd)
			return f"{customer.name} has successfully returned {dvd.name}"
		
		return f"{customer.name} does not have that DVD"
	
	def __repr__(self):
		result = ''
		for customer in self.customers:
			result += f"{repr(customer)}\n"
		for dvd in self.dvds:
			result += f"{repr(dvd)}\n"
		return result
