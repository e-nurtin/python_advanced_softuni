from project.appliances.appliance import Appliance


class Fridge(Appliance):
	@property
	def cost_per_unit(self):
		return 1.2
	
	def __init__(self):
		super().__init__(self.cost_per_unit)
		