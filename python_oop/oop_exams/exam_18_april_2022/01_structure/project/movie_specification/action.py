from project.movie_specification.movie import Movie


class Action(Movie):
	@property
	def allowed_min_age(self):
		return 12