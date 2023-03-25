from unittest import TestCase, main
from integer_list import IntegerList  # !This line should be removed or commented before submitting to judge system


class IntegerListTest(TestCase):
	def test_if_class_only_keeps_integers_in_list(self):
		int_list = IntegerList('a', 1, 2, 1.5)
		self.assertNotIn('a', int_list._IntegerList__data)
		self.assertNotIn(1.5, int_list._IntegerList__data)
		
		self.assertEqual([1, 2], int_list._IntegerList__data)
	
	def test_get_data_returns_list(self):
		int_list = IntegerList(1, 2)
		self.assertEqual([1, 2], int_list._IntegerList__data)
		
		result = int_list.get_data()
		self.assertEqual([1, 2], result)
	
	def test_add_method_wrong_type_raises(self):
		int_list = IntegerList(1, 2)
		self.assertEqual([1, 2], int_list._IntegerList__data)
		
		with self.assertRaises(ValueError) as exc:
			int_list.add('a')
		
		self.assertEqual("Element is not Integer", str(exc.exception))
	
	def test_add_method_correct_type(self):
		int_list = IntegerList(1, 2)
		self.assertEqual([1, 2], int_list._IntegerList__data)
		
		result = int_list.add(5)
		
		self.assertEqual([1, 2, 5], result)
	
	def test_remove_method_wrong_index_raises(self):
		int_list = IntegerList(1, 2)
		self.assertEqual([1, 2], int_list._IntegerList__data)
		
		with self.assertRaises(IndexError) as exc:
			int_list.remove_index(5)
		
		self.assertEqual("Index is out of range", str(exc.exception))
	
	def test_remove_method_correct_index(self):
		int_list = IntegerList(1, 2)
		self.assertEqual([1, 2], int_list._IntegerList__data)
		
		result = int_list.remove_index(1)
		self.assertEqual(2, result)
		self.assertEqual([1], int_list._IntegerList__data)
	
	def test_get_method_wrong_index_raises(self):
		int_list = IntegerList(1, 2)
		
		with self.assertRaises(IndexError) as exc:
			int_list.get(3)
		
		self.assertEqual("Index is out of range", str(exc.exception))
	
	def test_get_method_correct_index(self):
		int_list = IntegerList(1, 2)
		
		result = int_list.get(1)
		
		self.assertEqual(2, result)
	
	def test_insert_method_wrong_type_raises(self):
		int_list = IntegerList(1, 2)
		
		with self.assertRaises(ValueError) as exc:
			int_list.insert(0, 'a')
		
		self.assertEqual("Element is not Integer", str(exc.exception))
	
	def test_insert_method_wrong_index_raises(self):
		int_list = IntegerList(1, 2)
		
		with self.assertRaises(IndexError) as exc:
			int_list.insert(5, 2)
		
		self.assertEqual("Index is out of range", str(exc.exception))
	
	def test_insert_method_correct_input(self):
		int_list = IntegerList(1, 2)
		
		int_list.insert(0, 0)
		self.assertEqual([0, 1, 2], int_list._IntegerList__data)
	
	def test_get_biggest_method_returns(self):
		int_list = IntegerList(1, 3, 2)
		
		result = int_list.get_biggest()
		self.assertEqual(3, result)
	
	def test_get_index_from_element_returns(self):
		int_list = IntegerList(1, 3, 2)
		
		result = int_list.get_index(3)
		
		self.assertEqual(1, result)


if __name__ == '__main__':
	main()
