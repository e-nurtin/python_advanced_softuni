from project import Animal


class Dog(Animal):
	SOUND = 'Woof!'
	
	def __init__(self, name: str, age: int, gender: str):
		super().__init__(name, age, gender)
	
	def __repr__(self):
		return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}"
	
