from project.delicacies.delicacy import Delicacy


class Stolen(Delicacy):
	
	@property
	def portion(self):
		return 250
	
	@property
	def delicacy_type(self):
		return "Stolen"
