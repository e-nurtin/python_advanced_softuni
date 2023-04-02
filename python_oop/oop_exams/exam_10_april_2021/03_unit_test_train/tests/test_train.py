from project.train.train import Train
from unittest import TestCase, main


class TrainTest(TestCase):
	def setUp(self):
		self.train = Train('test', 10)
	
	def test_train_class_variables_set_correct(self):
		assert "Train is full" == self.train.TRAIN_FULL
		assert "Passenger {} Exists" == self.train.PASSENGER_EXISTS
		assert "Passenger Not Found" == self.train.PASSENGER_NOT_FOUND
		assert "Added passenger {}" == self.train.PASSENGER_ADD
		assert "Removed {}" == self.train.PASSENGER_REMOVED
		assert 0 == self.train.ZERO_CAPACITY
	
	def test_init_correct(self):
		assert 'test' == self.train.name
		assert 10 == self.train.capacity
		assert [] == self.train.passengers
		assert isinstance(self.train.passengers, list)
	
	def test_add_method_when_capacity_full_raises(self):
		self.train.passengers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
		
		with self.assertRaises(ValueError) as ex:
			self.train.add('name')
		
		assert "Train is full" == str(ex.exception)
	
	def test_add_method_with_same_name_exist_raises(self):
		self.train.add('name')
		
		with self.assertRaises(ValueError) as ex:
			self.train.add('name')
		
		assert "Passenger name Exists" == str(ex.exception)
	
	def test_add_method_adds_passenger(self):
		assert [] == self.train.passengers
		self.train.add('name1')
		self.train.add('name2')
		
		assert ['name1', 'name2'] == self.train.passengers
	
	def test_add_method_returns_correct__message(self):
		result = self.train.add('name')
		
		assert "Added passenger name" == result
	
	def test_remove_method_passenger_does_not_exist_raises(self):
		with self.assertRaises(ValueError) as ex:
			self.train.remove('passenger')
		
		assert "Passenger Not Found" == str(ex.exception)
	
	def test_remove_method_removes_passenger(self):
		self.train.add('passenger')
		self.train.add('passenger2')
		
		assert ['passenger', 'passenger2'] == self.train.passengers
		
		self.train.remove('passenger2')
		
		assert ['passenger'] == self.train.passengers
		
	def test_remove_method_returns_correct_message(self):
		self.train.add('passenger')
		self.train.add('passenger2')
		
		assert ['passenger', 'passenger2'] == self.train.passengers
		
		result = self.train.remove('passenger2')
		
		assert "Removed passenger2" == result


if __name__ == '__main__':
	main()
