from project.product import Product


class ProductRepository:
	def __init__(self):
		self.products = []
	
	def add(self, product):
		self.products.append(product)
	
	def find(self, product_name):
		# return next(filter(lambda x: x.name == product_name, self.products))
		for product in self.products:
			if product.name == product_name:
				return product.name
	
	def remove(self, product_name):
		for product in self.products:
			if product.name == product_name:
				self.products.remove(product)
		# self.products.remove(next(filter(lambda x: x.name == product_name, self.products)))
	
	def __repr__(self):
		result = [f"{x.name}: {x.quantity}" for x in self.products]
		return '\n'.join(result)
