class Room:
	def __init__(self, family_name: str, budget: float, members_count: int):
		self.family_name = family_name
		self.budget = budget
		self.members_count = members_count
		self.children = []
		self.expenses = 0
		self.room_cost = 0
		self.appliances = []
	
	@property
	def expenses(self):
		return self.__expenses
	
	@expenses.setter
	def expenses(self, value: int):
		if value < 0:
			raise ValueError("Expenses cannot be negative")
		self.__expenses = value
	
	def calculate_appliances(self):
		result = 0
		for appliance in self.appliances:
			result += appliance.get_monthly_expense()
		return result
	
	def calculate_expenses(self, *args):
		expenses = 0
		for element in args:
			expenses += element.cost * 30
		self.expenses = expenses
	
	def get_status(self):
		result = [
			f"{self.family_name} with {self.members_count} members. Budget: {self.budget:.2f}$, Expenses: {self.expenses:.2f}$"]
		
		if self.children:
			for number, child in enumerate(self.children, 1):
				result.append(f"--- Child {number} monthly cost: {child.cost * 30:.2f}$")
		result.append(f"--- Appliances monthly cost: {self.calculate_appliances():.2f}$")
		
		return '\n'.join(result)