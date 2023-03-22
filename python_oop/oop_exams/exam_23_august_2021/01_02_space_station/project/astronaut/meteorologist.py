from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
	def __init__(self, name):
		super().__init__(name, oxygen=90)
	
	@property
	def breath_units(self):
		return 15

