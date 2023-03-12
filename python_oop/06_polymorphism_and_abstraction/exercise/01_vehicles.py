from abc import ABC, abstractmethod


class Vehicle(ABC):
	def __init__(self, fuel_quantity, fuel_consumption):  # Quantity is given in liters
		self.fuel_quantity = fuel_quantity
		self.fuel_consumption = fuel_consumption
	
	@abstractmethod
	def drive(self, distance):
		pass
	
	@abstractmethod
	def refuel(self, fuel_quantity):
		pass
	

class Car(Vehicle):
	EXTRA_FUEL_FOR_AC_ON = 0.9

	def refuel(self, quantity):
		self.fuel_quantity += quantity
		
	def drive(self, distance):
		needed_fuel = (self.fuel_consumption + Car.EXTRA_FUEL_FOR_AC_ON) * distance
		
		if needed_fuel <= self.fuel_quantity:
			self.fuel_quantity -= needed_fuel


class Truck(Vehicle):
	EXTRA_FUEL_FOR_AC_ON = 1.6
	PROBLEM_IN_FUEL_TANK = 0.95
	
	def refuel(self, quantity):
		self.fuel_quantity += (quantity * Truck.PROBLEM_IN_FUEL_TANK)
	
	def drive(self, distance):
		needed_fuel = (self.fuel_consumption + Truck.EXTRA_FUEL_FOR_AC_ON) * distance
		
		if needed_fuel <= self.fuel_quantity:
			self.fuel_quantity -= needed_fuel


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
