from project.cat import Cat


class Tomcat(Cat):
	GENDER = 'Male'
	SOUND = 'Hiss'
	
	def __init__(self, name: str, age: int):
		super().__init__(name, age, Tomcat.GENDER)