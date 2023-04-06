from project.software.software import Software


class ExpressSoftware(Software):
	@property
	def type_of_software(self):
		return "Express"
	
	def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
		super().__init__(name, self.type_of_software, capacity_consumption, memory_consumption * 2)
	