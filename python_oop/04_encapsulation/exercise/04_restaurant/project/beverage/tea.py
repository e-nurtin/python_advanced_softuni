from project import HotBeverage


class Tea(HotBeverage):
	def __init__(self, name: str, price: int, milliliters: float):
		super().__init__(name, price, milliliters)