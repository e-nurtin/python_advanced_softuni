from project.appliances.appliance import Appliance


class TV(Appliance):
	@property
	def cost_per_unit(self):
		return 1.5
	
	def __init__(self):
		super().__init__(self.cost_per_unit)