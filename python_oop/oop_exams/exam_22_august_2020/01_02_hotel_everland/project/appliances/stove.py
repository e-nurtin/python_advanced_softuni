from project.appliances.appliance import Appliance


class Stove(Appliance):
	@property
	def cost_per_unit(self):
		return 0.7
	
	def __init__(self):
		super().__init__(self.cost_per_unit)