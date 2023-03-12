from project import Musician


class Singer(Musician):
	AVAILABLE_SKILLS = ["sing high pitch notes", "sing low pitch notes"]
	
	def __init__(self, name: str, age: int):
		super().__init__(name, age)

	