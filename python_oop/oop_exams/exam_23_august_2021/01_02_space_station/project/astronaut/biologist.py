from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
	def __init__(self, name):
		super().__init__(name, oxygen=70)
	
	@property
	def breath_units(self):
		return 5
	
