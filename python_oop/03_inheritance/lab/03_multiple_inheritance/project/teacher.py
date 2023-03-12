from project import Employee
from project import Person


class Teacher(Employee, Person):
	def teach(self):
		return 'teaching...'
	
	
	
	