class Zoo:
	def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
		self.name = name
		self.__budget = budget
		self.__animal_capacity = animal_capacity
		self.__workers_capacity = workers_capacity
		self.animals = []
		self.workers = []
	
	def add_animal(self, animal, price):
		if len(self.animals) >= self.__animal_capacity:
			return "Not enough space for animal"
		
		elif self.__budget < price:
			return "Not enough budget"
		
		self.animals.append(animal)
		self.__budget -= price
		return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
	
	def hire_worker(self, worker):
		if len(self.workers) >= self.__workers_capacity:
			return "Not enough space for worker"
		
		self.workers.append(worker)
		return f"{worker.name} the {worker.__class__.__name__} hired successfully"
	
	def fire_worker(self, worker_name):
		try:
			worker = next(filter(lambda w: w.name == worker_name, self.workers))
			self.workers.remove(worker)
			return f"{worker_name} fired successfully"
		
		except StopIteration:
			return f"There is no {worker_name} in the zoo"
	
	def pay_workers(self):
		budget_needed = sum([worker.salary for worker in self.workers])
		if budget_needed > self.__budget:
			return "You have no budget to pay your workers. They are unhappy"
		
		self.__budget -= budget_needed
		return f"You payed your workers. They are happy. Budget left: {self.__budget}"
	
	def tend_animals(self):
		money_needed = sum([animal.money_for_care for animal in self.animals])
		if money_needed > self.__budget:
			return "You have no budget to tend the animals. They are unhappy."
		
		self.__budget -= money_needed
		return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
	
	def profit(self, amount):
		self.__budget += amount
	
	def __build_entity_string(self, entities, entity_type):
		counter = 0
		result = ''
		for entity in entities:
			if entity.__class__.__name__ == entity_type:
				result += repr(entity) + '\n'
				counter += 1
		return f"----- {counter} {entity_type}s:\n" + result[:-1]
	
	def animals_status(self):
		order_of_animals = ['Lion', 'Tiger', 'Cheetah']
		result = f"You have {len(self.animals)} animals\n"
		
		for animal_type in order_of_animals:
			result += self.__build_entity_string(self.animals, animal_type)
		return result
	
	def workers_status(self):
		order_of_workers = ['Keeper', 'Caretaker', 'Vet']
		result = f"You have {len(self.workers)} workers\n"
		
		for worker_type in order_of_workers:
			result += self.__build_entity_string(self.workers, worker_type)
		return result

		
