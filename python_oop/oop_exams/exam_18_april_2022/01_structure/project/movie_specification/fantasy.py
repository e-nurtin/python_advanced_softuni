from project.movie_specification.movie import Movie


class Fantasy(Movie):
	@property
	def allowed_min_age(self):
		return 6
