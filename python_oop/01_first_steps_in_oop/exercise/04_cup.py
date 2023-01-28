class Cup:
	def __init__(self, size: int, quantity: int):
		self.size = size
		self.quantity = quantity
		
	def fill(self, milliliters: int):
		if self.quantity + milliliters <= self.size:
			self.quantity += milliliters
			
	def status(self):
		return self.size - self.quantity
	
