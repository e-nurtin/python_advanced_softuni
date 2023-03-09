from abc import ABC, abstractmethod


class Tax(ABC):
	@abstractmethod
	def calculate_tax(self, annual_income):
		pass


class Person(Tax):
	def __init__(self, name, age):
		self.name = name
		self.age = age
	
	def calculate_tax(self, annual_income):
		return annual_income * 0.2


class Chef(Person):
	def __init__(self, name, age, annual_income):
		super().__init__(name, age)
		self.annual_income = annual_income
	
	def calculate_tax(self, annual_income):
		return annual_income * 0.2


class Attorney(Person):
	def __init__(self, name, age, annual_income):
		super().__init__(name, age)
		self.annual_income = annual_income
	
	def calculate_tax(self, annual_income):
		return annual_income * 0.2


class Employee(Person):
	def __init__(self, name, age, annual_income):
		super().__init__(name, age)
		self.annual_income = annual_income
	
	def calculate_tax(self, annual_income):
		return annual_income * 0.2


employees = [Employee('mark', 30, 21000), Chef("Max", 28, 30600), Attorney("Helen", 43, 35000)]

for employee in employees:
	print(employee.calculate_tax(employee.annual_income))
