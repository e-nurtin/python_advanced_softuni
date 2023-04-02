from project.shopping_cart import ShoppingCart
from unittest import TestCase, main


class TestShoppingCart(TestCase):
	def setUp(self):
		self.sp_cart = ShoppingCart('Shop', 100)
	
	def test_init(self):
		assert 'Shop' == self.sp_cart.shop_name
		assert 100 == self.sp_cart.budget
		assert isinstance(self.sp_cart.products, dict)
		assert {} == self.sp_cart.products
	
	def test_shop_name_setter_does_not_start_with_capital_letter_raises(self):
		with self.assertRaises(ValueError) as ex:
			self.sp_cart.shop_name = 'shop'
		expected_msg = "Shop must contain only letters and must start with capital letter!"
		assert expected_msg == str(ex.exception)
	
	def test_shop_name_setter_contains_numbers_raises(self):
		with self.assertRaises(ValueError) as ex:
			self.sp_cart.shop_name = 'shop1'
		expected_msg = "Shop must contain only letters and must start with capital letter!"
		assert expected_msg == str(ex.exception)
	
	def test_add_to_cart_method_product_cost_high_raises(self):
		with self.assertRaises(ValueError) as ex:
			self.sp_cart.add_to_cart('product', 101)
		expected_msg = f"Product product cost too much!"
		assert expected_msg == str(ex.exception)
	
	def test_add_to_cart_method_product_cost_equal_to_100_raises(self):
		with self.assertRaises(ValueError) as ex:
			self.sp_cart.add_to_cart('product', 100)
		expected_msg = f"Product product cost too much!"
		assert expected_msg == str(ex.exception)
	
	def test_add_to_cart_method_product_adds(self):
		self.sp_cart.add_to_cart('product', 20)
		assert {'product': 20} == self.sp_cart.products
		self.sp_cart.add_to_cart('product2', 50)
		assert {'product': 20, 'product2': 50} == self.sp_cart.products
	
	def test_add_to_cart_method_returns_msg_after_adding(self):
		self.sp_cart.add_to_cart('product', 20)
		result = self.sp_cart.add_to_cart('product2', 50)
		expected = "product2 product was successfully added to the cart!"
		
		assert expected == result
	
	def test_remove_from_cart_product_not_in_cart_raises(self):
		with self.assertRaises(ValueError) as ex:
			self.sp_cart.remove_from_cart('product')
		
		expected = "No product with name product in the cart!"
		assert expected == str(ex.exception)
	
	def test_remove_from_cart_removes_product_from_cart(self):
		self.sp_cart.add_to_cart('product', 20)
		self.sp_cart.add_to_cart('product2', 50)
		assert {'product': 20, 'product2': 50} == self.sp_cart.products
		self.sp_cart.remove_from_cart('product')
		assert {'product2': 50} == self.sp_cart.products
	
	def test_remove_from_cart_returns_correct_message(self):
		self.sp_cart.add_to_cart('product', 20)
		self.sp_cart.add_to_cart('product2', 50)
		result = self.sp_cart.remove_from_cart('product')
		expected = "Product product was successfully removed from the cart!"
		assert expected == result
	
	def test_if__add__dunder_method_works(self):
		other_cart = ShoppingCart('Top', 100)
		self.sp_cart.products = {'product1': 20, 'product2': 30}
		other_cart.products = {'procus': 11, 'corus': 22}
		
		new_cart = self.sp_cart + other_cart
		
		assert 200 == new_cart.budget
		assert {'product1': 20, 'product2': 30, 'procus': 11, 'corus': 22} == new_cart.products
	
	def test_buy_products_total_sum_too_high_raises(self):
		self.sp_cart.add_to_cart('product', 20)
		self.sp_cart.add_to_cart('product2', 50)
		self.sp_cart.add_to_cart('product3', 50)
		
		with self.assertRaises(ValueError) as ex:
			self.sp_cart.buy_products()
		
		expected = "Not enough money to buy the products! Over budget with 20.00lv!"
		assert expected == str(ex.exception)
	
	def test_buy_products_returns_correct_message(self):
		self.sp_cart.add_to_cart('product', 20)
		self.sp_cart.add_to_cart('product3', 50)
		
		result = self.sp_cart.buy_products()
		expected = "Products were successfully bought! Total cost: 70.00lv."
		assert expected == result


if __name__ == '__main__':
	main()
