from project.delicacies.delicacy import Delicacy


class Stolen(Delicacy):
	def __init__(self, name: str, price: float):
		super().__init__(name, price)
		self.portion = 250
		