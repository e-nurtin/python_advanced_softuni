from calendar import month_name


class DVD:
	def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int):
		self.name = name
		self.id = id
		self.creation_year = creation_year
		self.creation_month = creation_month
		self.age_restriction = age_restriction
		self.is_rented = False
	
	@property
	def status(self):
		if self.is_rented:
			return "rented"
		return "not rented"
	
	@classmethod
	def from_date(cls, id: int, name: str, date: str, age_restriction: int):
		day, month, year = date.split('.')
		month = month_name[int(month)]
		return cls(name, id, int(year), month, age_restriction)
	
	def __repr__(self):
		return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: {self.status}"
	
