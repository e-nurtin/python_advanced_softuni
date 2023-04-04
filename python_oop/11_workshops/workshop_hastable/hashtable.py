class HashTable:
	
	def __init__(self):
		self.__capacity = 4
		self.keys = [None] * self.__capacity
		self.values = [None] * self.__capacity
	
	def hash(self, key, value, index):
		if key in self.keys:
			index = self.__find_index(key)
			self.values[index] = value
			return
		
		if len(self) == self.__capacity:
			self.__adjust_capacity()
		
		if index == len(self.keys):
			index = self.__check_if_index_is_correct(0)
		
		index = self.__check_if_index_is_correct(index)
		
		self.keys[index] = key
		self.values[index] = value
	
	def get(self, key, default=None):
		try:
			index = self.__find_index(key)
			return self.values[index]
		except ValueError:
			return default
	
	def __setitem__(self, key, value):
		index = self.__calc_index(key)
		self.hash(key, value, index)
	
	def __getitem__(self, key):
		if key not in self.keys:
			raise KeyError(f"'{key}' not found in hashtable!")
		index = self.__find_index(key)
		return self.values[index]
	
	def __delitem__(self, key):
		if key not in self.keys:
			raise KeyError(f"'{key}' not found in hashtable!")
		index = self.__find_index(key)
		self.keys[index] = None
		self.values[index] = None
	
	def __len__(self):
		return sum(1 for key in self.keys if key is not None)
	
	def __calc_index(self, key):
		return sum(ord(c) for c in key) % self.__capacity
	
	def __check_if_index_is_correct(self, index):
		if index == len(self.keys):
			index = 0
		
		if self.keys[index] is not None:
			return self.__check_if_index_is_correct(index + 1)
		
		return index
	
	def __adjust_capacity(self):
		self.keys = self.keys + [None] * self.__capacity
		self.values = self.values + [None] * self.__capacity
		self.__capacity *= 2
	
	def __find_index(self, key):
		return self.keys.index(key)
	
	def __str__(self):
		result = []
		
		for index, key in enumerate(self.keys):
			if key is not None:
				result.append(f"{key}: {self.values[index]}")
		
		return '{' + ', '.join(result) + '}'


table = HashTable()

table["name"] = "Peter"
table["age"] = 25
table['aa'] = 12
table['ba'] = 132
table['asd'] = 'a'

table['ssss'] = table.get('ssss', 'default valueeee')
del table['ba']

print(table.get("name"))
print(table["age"])
print(len(table))
print(table)
