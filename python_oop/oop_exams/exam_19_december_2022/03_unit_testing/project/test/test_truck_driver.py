from project.truck_driver import TruckDriver
from unittest import TestCase, main


class TestTruckDriver(TestCase):
	def setUp(self):
		self.truck_driver = TruckDriver('Test', 10)
		
	def test_init(self):
		self.assertEqual('Test', self.truck_driver.name)
		self.assertEqual(10, self.truck_driver.money_per_mile)
		self.assertEqual(dict, type(self.truck_driver.available_cargos))
		self.assertEqual({}, self.truck_driver.available_cargos)
		self.assertEqual(0, self.truck_driver.earned_money)
		self.assertEqual(0, self.truck_driver.miles)

	def test_earned_money_setter_raises(self):
		with self.assertRaises(ValueError) as exc:
			self.truck_driver.earned_money = -2
		self.assertEqual(f"Test went bankrupt.", str(exc.exception))
	
	def test_earned_money_setter_sets_earned_money(self):
		self.truck_driver.earned_money = 5
		self.assertEqual(5, self.truck_driver.earned_money)
	
	def test_add_cargo_offer_raises(self):
		self.truck_driver.add_cargo_offer('location', 100)
		with self.assertRaises(Exception) as exc:
			self.truck_driver.add_cargo_offer('location', 100)
		
		self.assertEqual("Cargo offer is already added.", str(exc.exception))
		
	def test_add_cargo_sets_correct_dict(self):
		self.truck_driver.add_cargo_offer('location', 100)
		self.assertEqual({'location': 100}, self.truck_driver.available_cargos)
		
	def test_add_cargo_returns_correct_msg(self):
		result = self.truck_driver.add_cargo_offer('location', 100)
		expected = "Cargo for 100 to location was added as an offer."
		self.assertEqual(expected, result)

	def test_drive_best_cargo_offer_no_offers_catches_error(self):
		result = self.truck_driver.drive_best_cargo_offer()
		expected = "There are no offers available."
		self.assertEqual(expected, result)
		
	def test_drive_best_cargo_offer_gets_best_offer(self):
		self.truck_driver.add_cargo_offer('location', 100)
		self.truck_driver.add_cargo_offer('location2', 150)
		
		self.truck_driver.drive_best_cargo_offer()
		self.assertEqual(1500, self.truck_driver.earned_money)
		self.assertEqual(150, self.truck_driver.miles)
	
	def test_drive_best_cargo_offer_returns_correct_msg(self):
		self.truck_driver.add_cargo_offer('location', 150)
		self.truck_driver.add_cargo_offer('location2', 100)
		
		result = self.truck_driver.drive_best_cargo_offer()
		expected = "Test is driving 150 to location."
		self.assertEqual(expected, result)
	
	def test_drive_best_cargo_offer_calls_check_for_activities(self):
		self.truck_driver.add_cargo_offer('location', 150)
		self.truck_driver.add_cargo_offer('location2', 100)
		
		self.truck_driver.drive_best_cargo_offer()
		self.assertEqual(150, self.truck_driver.miles)
		self.assertEqual(1500, self.truck_driver.earned_money)
		self.assertEqual({'location': 150, 'location2': 100}, self.truck_driver.available_cargos)
		
	def test_eat_method_works(self):
		self.truck_driver.earned_money = 50
		self.truck_driver.eat(250)
		
		self.assertEqual(30, self.truck_driver.earned_money)
	
	def test_sleep_method_works(self):
		self.truck_driver.earned_money = 50
		self.truck_driver.sleep(1000)
		
		self.assertEqual(5, self.truck_driver.earned_money)
	
	def test_pump_gas_method_works(self):
		self.truck_driver.earned_money = 501
		self.truck_driver.pump_gas(1500)
		
		self.assertEqual(1, self.truck_driver.earned_money)
	
	def test_repair_truck_method_works(self):
		self.truck_driver.earned_money = 7505
		self.truck_driver.repair_truck(10000)
		
		self.assertEqual(5, self.truck_driver.earned_money)
	
	def test_if_check_for_activities_calls_all_other_methods(self):
		self.truck_driver.earned_money = 11800
		self.truck_driver.check_for_activities(10000)

		self.assertEqual(50, self.truck_driver.earned_money)
		
	# def test_if_check_for_activities_raises(self):
	# 	self.truck_driver.earned_money = 5000
	# 	with self.assertRaises(ValueError) as ex:
	# 		pass
	#
	# 	self.assertEqual(50, self.truck_driver.earned_money)

	def test_repr_returns_correct_message(self):
		self.assertEqual("Test has 0 miles behind his back.", str(self.truck_driver))
		
		
if __name__ == '__main__':
	main()
