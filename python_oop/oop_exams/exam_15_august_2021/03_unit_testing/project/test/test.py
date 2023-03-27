from project.pet_shop import PetShop
from unittest import TestCase, main


class PetShopTests(TestCase):
	def test_pet_shop_init_name_property(self):
		pet_shop = PetShop('pet shop')
		
		self.assertEqual('pet shop', pet_shop.name)
	
	def test_pet_shop_init_food_dict_returns(self):
		pet_shop = PetShop('pet shop')
		
		self.assertEqual({}, pet_shop.food)
	
	def test_pet_shop_init_pets_list_returns(self):
		pet_shop = PetShop('pet shop')
		
		self.assertEqual([], pet_shop.pets)
	
	def test_add_food_method_zero_quantity_raises(self):
		pet_shop = PetShop('pet shop')
		
		with self.assertRaises(ValueError) as exc:
			pet_shop.add_food('dog food', 0.0)
		
		expected = 'Quantity cannot be equal to or less than 0'
		result = str(exc.exception)
		
		self.assertEqual(expected, result)
	
	def test_add_food_method_negative_quantity_raises(self):
		pet_shop = PetShop('pet shop')
		
		with self.assertRaises(ValueError) as exc:
			pet_shop.add_food('dog food', -330.0)
		
		expected = 'Quantity cannot be equal to or less than 0'
		result = str(exc.exception)
		
		self.assertEqual(expected, result)
	
	def test_add_food_method_add_quantity(self):
		pet_shop = PetShop('pet shop')
		self.assertEqual({}, pet_shop.food)
		
		pet_shop.add_food('dog food', 1000.00)
		expected = {'dog food': 1000.00}
		
		self.assertEqual(expected, pet_shop.food)
	
	def test_add_food_method_add_quantity_returns(self):
		pet_shop = PetShop('pet shop')
		self.assertEqual({}, pet_shop.food)
		
		result = pet_shop.add_food('dog food', 1000.00)
		expected = "Successfully added 1000.00 grams of dog food."
		
		self.assertEqual(expected, result)
	
	def test_add_pet_method_add_with_same_name_raises(self):
		pet_shop = PetShop('pet shop')
		pet_shop.add_pet('cat')
		
		with self.assertRaises(Exception) as exc:
			pet_shop.add_pet('cat')
		
		expected = "Cannot add a pet with the same name"
		result = str(exc.exception)
		
		self.assertEqual(expected, result)
	
	def test_add_pet_method_adds_pet(self):
		pet_shop = PetShop('pet shop')
		
		pet_shop.add_pet('cat')
		self.assertEqual(['cat'], pet_shop.pets)
		
		pet_shop.add_pet('another cat')
		self.assertEqual(['cat', 'another cat'], pet_shop.pets)
	
	def test_add_pet_method_returns_msg(self):
		pet_shop = PetShop('pet shop')
		self.assertEqual([], pet_shop.pets)
		
		result = pet_shop.add_pet('cat')
		expected = "Successfully added cat."
		
		self.assertEqual(expected, result)
	
	def test_feed_pet_method_pet_not_found_raises(self):
		pet_shop = PetShop('pet shop')
		pet_shop.add_food('cat food', 1000.00)
		
		with self.assertRaises(Exception) as exc:
			pet_shop.feed_pet('cat food', 'cat')
		
		expected = "Please insert a valid pet name"
		result = str(exc.exception)
		
		self.assertEqual(expected, result)
	
	def test_feed_pet_method_food_not_found_returns(self):
		pet_shop = PetShop('pet shop')
		pet_shop.add_pet('cat')
		
		result = pet_shop.feed_pet('cat food', 'cat')
		expected = "You do not have cat food"
		
		self.assertEqual(expected, result)
	
	def test_feed_pet_method_food_not_enough_add_food_returns(self):
		pet_shop = PetShop('pet shop')
		pet_shop.add_pet('cat')
		pet_shop.add_food('cat food', 50.00)
		
		result = pet_shop.feed_pet('cat food', 'cat')
		expected = "Adding food..."
		
		self.assertEqual(expected, result)
	
	def test_feed_pet_method_food_not_enough_adds_food(self):
		pet_shop = PetShop('pet shop')
		pet_shop.add_pet('cat')
		pet_shop.add_food('cat food', 50.00)
		
		self.assertEqual(50.00, pet_shop.food['cat food'])
		pet_shop.feed_pet('cat food', 'cat')
		
		self.assertEqual(1050.00, pet_shop.food['cat food'])
	
	def test_feed_pet_method_feeds_pet(self):
		pet_shop = PetShop('pet shop')
		pet_shop.add_pet('cat')
		
		pet_shop.add_food('cat food', 150.00)
		self.assertEqual(150.00, pet_shop.food['cat food'])
		
		pet_shop.feed_pet('cat food', 'cat')
		self.assertEqual(50.00, pet_shop.food['cat food'])
	
	def test_feed_pet_method_returns(self):
		pet_shop = PetShop('pet shop')
		pet_shop.add_pet('cat')
		pet_shop.add_food('cat food', 150.00)
		
		result = pet_shop.feed_pet('cat food', 'cat')
		expected = "cat was successfully fed"
		
		self.assertEqual(expected, result)
	
	def test_repr_method_returns(self):
		pet_shop = PetShop('pet shop')
		pet_shop.add_pet('cat')
		pet_shop.add_pet('dog')
		pet_shop.add_food('cat food', 150.00)
		
		expected = 'Shop pet shop:\nPets: cat, dog'
		result = str(pet_shop)
		
		self.assertEqual(expected, result)
		
		
if __name__ == "__main__":
	main()