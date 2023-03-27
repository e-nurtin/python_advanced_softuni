from project.toy_store import ToyStore
from unittest import TestCase, main


class ToyStoreTests(TestCase):
	def test_init_method_default_dict(self):
		toy_store = ToyStore()
		
		expected = {}
		for i in range(65, 72):
			expected[chr(i)] = None
		
		self.assertEqual(expected, toy_store.toy_shelf)
	
	def test_add_toy_method_wrong_shelf_raises(self):
		toy_store = ToyStore()
		expected = "Shelf doesn't exist!"
		
		with self.assertRaises(Exception) as exc:
			toy_store.add_toy('Z', 'Teddy Bear')
		
		result = str(exc.exception)
		self.assertEqual(expected, result)
	
	def test_add_toy_method_toy_already_in_shelf_raises(self):
		toy_store = ToyStore()
		toy_store.add_toy('A', 'Teddy Bear')
		
		expected = "Toy is already in shelf!"
		
		with self.assertRaises(Exception) as exc:
			toy_store.add_toy('A', 'Teddy Bear')
		
		result = str(exc.exception)
		self.assertEqual(expected, result)
	
	def test_add_toy_method_shelf_already_taken_raises(self):
		toy_store = ToyStore()
		toy_store.add_toy('A', 'Teddy Bear')
		
		expected = "Shelf is already taken!"
		
		with self.assertRaises(Exception) as exc:
			toy_store.add_toy('A', 'Bear Toy')
		
		result = str(exc.exception)
		self.assertEqual(expected, result)
	
	def test_add_toy_method_updates_toy_shelf(self):
		toy_store = ToyStore()
		toy_store.add_toy('A', 'Teddy Bear')
		
		expected = {}
		for i in range(65, 72):
			expected[chr(i)] = None
		expected['A'] = 'Teddy Bear'
		
		self.assertEqual(expected, toy_store.toy_shelf)
	
	def test_add_toy_method_returns_msg(self):
		toy_store = ToyStore()
		
		expected = "Toy:Teddy Bear placed successfully!"
		result = toy_store.add_toy('A', 'Teddy Bear')
		
		self.assertEqual(expected, result)
	
	def test_remove_toy_method_wrong_shelf_raises(self):
		toy_store = ToyStore()
		toy_store.add_toy('A', 'Teddy Bear')
		
		with self.assertRaises(Exception) as exc:
			toy_store.remove_toy('Z', 'Teddy Bear')
		
		expected = "Shelf doesn't exist!"
		result = str(exc.exception)
		
		self.assertEqual(expected, result)
	
	def test_remove_toy_method_wrong_toy_raises(self):
		toy_store = ToyStore()
		toy_store.add_toy('A', 'Teddy Bear')
		
		with self.assertRaises(Exception) as exc:
			toy_store.remove_toy('A', 'Bear')
		
		expected = "Toy in that shelf doesn't exists!"
		result = str(exc.exception)
		
		self.assertEqual(expected, result)
	
	def test_remove_toy_method_updates_shelf(self):
		toy_store = ToyStore()
		expected = {}
		for i in range(65, 72):
			expected[chr(i)] = None
		
		self.assertEqual(expected, toy_store.toy_shelf)
		
		expected['A'] = 'Teddy Bear'
		toy_store.add_toy('A', 'Teddy Bear')
		
		self.assertEqual(expected, toy_store.toy_shelf)
		
		toy_store.remove_toy('A', 'Teddy Bear')
		expected['A'] = None
		
		self.assertEqual(expected, toy_store.toy_shelf)
		
	def test_remove_toy_method_returns_msg(self):
		toy_store = ToyStore()
		toy_store.add_toy('A', 'Teddy Bear')
		
		result = toy_store.remove_toy('A', 'Teddy Bear')
		expected = "Remove toy:Teddy Bear successfully!"
		
		self.assertEqual(expected, result)
		

if __name__ == '__main__':
	main()
