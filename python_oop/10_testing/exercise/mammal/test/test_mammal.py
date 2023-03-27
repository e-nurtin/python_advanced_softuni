from unittest import TestCase, main
from project.mammal import Mammal


class MammalTests(TestCase):
	def test_mammal_init_name(self):
		mammal = Mammal('name', 'mammal', 'sound')
		
		self.assertEqual('name', mammal.name)
	
	def test_mammal_init_mammal_type(self):
		mammal = Mammal('name', 'mammal', 'sound')
		
		self.assertEqual('mammal', mammal.type)
		
	def test_mammal_init_sound(self):
		mammal = Mammal('name', 'mammal', 'sound')
		
		self.assertEqual('sound', mammal.sound)
		
	def test_mammal_private_attr_kingdom(self):
		mammal = Mammal('name', 'mammal', 'sound')
		
		self.assertEqual('animals', mammal._Mammal__kingdom)
		
	def test_make_sound_method(self):
		mammal = Mammal('name', 'mammal', 'sound')
		
		self.assertEqual("name makes sound", mammal.make_sound())
		
	def test_get_kingdom_method(self):
		mammal = Mammal('name', 'mammal', 'sound')
		
		self.assertEqual('animals', mammal.get_kingdom())
		
	def test_info_method(self):
		mammal = Mammal('name', 'mammal', 'sound')
		
		self.assertEqual('name is of type mammal', mammal.info())
		

if __name__ == '__main__':
	main()
