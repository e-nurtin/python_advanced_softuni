from project.delicacies.delicacy import Delicacy


class Gingerbread(Delicacy):
	
	@property
	def portion(self):
		return 200
	
	@property
	def delicacy_type(self):
		return "Gingerbread"