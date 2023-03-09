class IdMixin:
	
	@classmethod
	def get_next_id(cls):
		result = cls.id
		cls.id += 1
		return result