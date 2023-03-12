from project import Cat


class Kitten(Cat):
	GENDER = 'Female'
	SOUND = 'Meow'
	
	def __init__(self, name: str, age: int):
		super().__init__(name, age, Kitten.GENDER)