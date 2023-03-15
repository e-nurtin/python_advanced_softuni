from project.movie_specification.movie import Movie


class Thriller(Movie):
	@property
	def allowed_min_age(self):
		return 16
	