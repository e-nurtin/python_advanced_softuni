from unittest import TestCase, main
from project.factory.factory import Factory
from project.factory.paint_factory import PaintFactory


class TestPaintFactory(TestCase):
	def setUp(self):
		self.factory = PaintFactory("factory", 100)
	
	def test_if_base_class_is_abstract(self):
		with self.assertRaises(TypeError) as type_error:
			factory = Factory('name', 5)
		expected = "Can't instantiate abstract class Factory with abstract methods __init__, add_ingredient, remove_ingredient"
		result = str(type_error.exception)
		self.assertEqual(expected, result)
	
	def test_init_paint_factory(self):
		assert 'factory' == self.factory.name
		assert 100 == self.factory.capacity
		assert isinstance(self.factory.ingredients, dict)
		assert isinstance(self.factory.valid_ingredients, list)
		assert ["white", "yellow", "blue", "green", "red"] == self.factory.valid_ingredients
	
	def test_add_ingredient_method_invalid_ingredient_raises(self):
		with self.assertRaises(TypeError) as type_error:
			self.factory.add_ingredient('orange', 50)
		
		expected = f"Ingredient of type orange not allowed in PaintFactory"
		self.assertEqual(expected, str(type_error.exception))
	
	def test_add_ingredient_method_not_enough_capacity_raises(self):
		with self.assertRaises(ValueError) as ex:
			self.factory.add_ingredient('yellow', 150)
		
		expected = "Not enough space in factory"
		self.assertEqual(expected, str(ex.exception))
	
	def test_can_add_method_returns_correct_value(self):
		self.factory.ingredients = {'yellow': 20, 'blue': 20, 'green': 20}
		
		self.assertTrue(self.factory.can_add(20))
		self.assertFalse(self.factory.can_add(50))
	
	def test_add_ingredient_adds_ingredients_to_dict(self):
		self.factory.add_ingredient('white', 20)
		self.assertEqual({'white': 20}, self.factory.ingredients)
		
		self.factory.add_ingredient('white', 20)
		self.factory.add_ingredient('yellow', 20)
		self.assertEqual({'white': 40, 'yellow': 20}, self.factory.ingredients)
	
	def test_remove_ingredient_product_not_in_dict_raises(self):
		with self.assertRaises(KeyError) as ex:
			self.factory.remove_ingredient('white', 10)
		
		expected = "'No such ingredient in the factory'"
		self.assertEqual(expected, str(ex.exception))
	
	def test_remove_ingredient_with_insufficient_quantity_raises(self):
		self.factory.add_ingredient('white', 20)
		
		with self.assertRaises(ValueError) as ex:
			self.factory.remove_ingredient('white', 30)
		
		expected = "Ingredients quantity cannot be less than zero"
		self.assertEqual(expected, str(ex.exception))
	
	def test_remove_ingredient_removes_given_quantity(self):
		self.factory.add_ingredient('white', 50)
		self.assertEqual({'white': 50}, self.factory.ingredients)
		
		self.factory.remove_ingredient('white', 30)
		
		self.assertEqual({'white': 20}, self.factory.ingredients)
	
	def test_products_property_returns_ingredients(self):
		self.factory.add_ingredient('white', 20)
		self.factory.add_ingredient('yellow', 20)
		
		self.assertEqual({'white': 20, 'yellow': 20}, self.factory.products)
	
	def test__repr__returns_correct_message(self):
		self.factory.add_ingredient('white', 20)
		self.factory.add_ingredient('yellow', 20)
		
		expected = "Factory name: factory with capacity 100.\nwhite: 20\nyellow: 20\n"
		result = str(self.factory)
		
		self.assertEqual(expected, result)


if __name__ == '__main__':
	main()
