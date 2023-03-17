from project.movie_specification.movie import Movie


class Action(Movie):
	def __init__(self, title: str, year: int, owner: object, age_restriction: int = 12):
		super().__init__(title, year, owner, age_restriction)
		
	@property
	def allowed_min_age(self):
		return 12