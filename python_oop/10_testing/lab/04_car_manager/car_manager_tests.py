from unittest import TestCase, main
from car_manager import Car  # !This line should be removed or commented before submitting to judge system


class CarManagerTests(TestCase):
	def test_car_manager_init_with_wrong_make(self):
		with self.assertRaises(Exception) as exc:
			Car('', 'model', 5, 3)
		
		self.assertEqual("Make cannot be null or empty!", str(exc.exception))
	
	def test_car_manager_init_with_correct_make(self):
		car = Car('make', 'model', 5, 3)
		
		self.assertEqual('make', car.make)
	
	def test_car_manager_init_with_wrong_model(self):
		with self.assertRaises(Exception) as exc:
			Car('make', '', 5, 3)
		
		self.assertEqual("Model cannot be null or empty!", str(exc.exception))
	
	def test_car_manager_init_with_correct_model(self):
		car = Car('make', 'model', 5, 3)
		
		self.assertEqual('model', car.model)
	
	def test_car_manager_init_fuel_consumption_with_zero(self):
		with self.assertRaises(Exception) as exc:
			Car('make', 'model', 0, 5)
		
		self.assertEqual("Fuel consumption cannot be zero or negative!", str(exc.exception))
	
	def test_car_manager_init_fuel_consumption_with_negative(self):
		with self.assertRaises(Exception) as exc:
			Car('make', 'model', -5, 5)
		
		self.assertEqual("Fuel consumption cannot be zero or negative!", str(exc.exception))
	
	def test_car_manager_init_fuel_consumption_with_positive(self):
		car = Car('make', 'model', 5, 3)
		
		self.assertEqual(5, car.fuel_consumption)
	
	def test_car_manager_init_fuel_capacity_with_zero(self):
		with self.assertRaises(Exception) as exc:
			Car('make', 'model', 5, 0)
		
		self.assertEqual("Fuel capacity cannot be zero or negative!", str(exc.exception))
	
	def test_car_manager_init_fuel_capacity_with_negative(self):
		with self.assertRaises(Exception) as exc:
			Car('make', 'model', 5, -5)
		
		self.assertEqual("Fuel capacity cannot be zero or negative!", str(exc.exception))
	
	def test_car_manager_init_fuel_capacity_with_positive(self):
		car = Car('make', 'model', 3, 5)
		
		self.assertEqual(5, car.fuel_capacity)
	
	def test_car_manager_init_fuel_amount(self):
		car = Car('make', 'model', 3, 5)
		
		self.assertEqual(0, car.fuel_amount)
	
	def test_car_manager_init_fuel_amount_change_with_negative(self):
		car = Car('make', 'model', 3, 5)
		
		with self.assertRaises(Exception) as exc:
			car.fuel_amount = -5
		
		self.assertEqual("Fuel amount cannot be negative!", str(exc.exception))
	
	def test_car_manager_init_fuel_amount_change_with_positive(self):
		car = Car('make', 'model', 3, 5)
		
		car.fuel_amount = 5
		self.assertEqual(5, car.fuel_amount)
	
	def test_refuel_method_with_negative_fuel_amount(self):
		car = Car('make', 'model', 3, 5)
		
		with self.assertRaises(Exception) as exc:
			car.refuel(-3)
		
		self.assertEqual("Fuel amount cannot be zero or negative!", str(exc.exception))
	
	def test_refuel_method_with_zero_fuel_amount(self):
		car = Car('make', 'model', 3, 5)
		
		with self.assertRaises(Exception) as exc:
			car.refuel(0)
		
		self.assertEqual("Fuel amount cannot be zero or negative!", str(exc.exception))
	
	def test_refuel_method_with_positive_fuel_amount(self):
		car = Car('make', 'model', 3, 5)
		self.assertEqual(0, car.fuel_amount)
		
		car.refuel(2)
		self.assertEqual(2, car.fuel_amount)
	
	def test_refuel_method_with_excessive_fuel_amount(self):
		car = Car('make', 'model', 3, 5)
		self.assertEqual(0, car.fuel_amount)
		
		car.refuel(12)
		self.assertEqual(5, car.fuel_amount)
	
	def test_drive_method_with_too_big_distance_raises(self):
		car = Car('make', 'model', 3, 5)
		car.refuel(5)
		
		with self.assertRaises(Exception) as exc:
			car.drive(300)
		
		self.assertEqual("You don't have enough fuel to drive!", str(exc.exception))
	
	def test_drive_method_with_normal_distance_if_fuel_decreased(self):
		car = Car('make', 'model', 3, 5)
		car.refuel(5)
		self.assertEqual(5, car.fuel_amount)
		
		car.drive(100)
		self.assertEqual(2, car.fuel_amount)


if __name__ == '__main__':
	main()
