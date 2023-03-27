from project.vehicle import Vehicle
from unittest import TestCase, main


class VehicleTests(TestCase):
	def test_class_attr_default_fuel_consumption(self):
		vehicle = Vehicle(20, 140)
		self.assertEqual(1.25, vehicle.DEFAULT_FUEL_CONSUMPTION)
	
	def test_vehicle_init_fuel(self):
		vehicle = Vehicle(20, 140)
		self.assertEqual(20, vehicle.fuel)
		
	def test_vehicle_init_horse_power(self):
		vehicle = Vehicle(20, 140)
		self.assertEqual(140, vehicle.horse_power)
	
	def test_vehicle_init_capacity(self):
		vehicle = Vehicle(20, 140)
		self.assertEqual(20, vehicle.capacity)
		
	def test_vehicle_drive_method_with_too_long_distance(self):
		vehicle = Vehicle(20, 140)
		
		with self.assertRaises(Exception) as exc:
			vehicle.drive(500)
		
		self.assertEqual("Not enough fuel", str(exc.exception))
		
	def test_vehicle_drive_method_with_normal_distance(self):
		vehicle = Vehicle(80, 140)
		self.assertEqual(80, vehicle.fuel)
		
		vehicle.drive(10)
		self.assertEqual(67.5, vehicle.fuel)

	def test_vehicle_refuel_method_with_too_much_fuel_raises(self):
		vehicle = Vehicle(20, 140)
		
		with self.assertRaises(Exception) as exc:
			vehicle.refuel(100)
		
		self.assertEqual('Too much fuel', str(exc.exception))
	
	def test_vehicle_refuel_method_with_normal_fuel_works(self):
		vehicle = Vehicle(20, 140)
		self.assertEqual(20, vehicle.fuel)
		
		vehicle.drive(10)
		self.assertEqual(7.5, vehicle.fuel)
		
		vehicle.refuel(10)
		self.assertEqual(17.5, vehicle.fuel)
		
	def test_vehicle_str_method_returns(self):
		vehicle = Vehicle(20, 140)
		expected = "The vehicle has 140 horse power with 20 fuel left and 1.25 fuel consumption"
		result = str(vehicle)
		self.assertEqual(expected, result)
		
		
if __name__ == '__main__':
	main()
