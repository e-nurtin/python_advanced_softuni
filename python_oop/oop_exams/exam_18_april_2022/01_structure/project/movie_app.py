from typing import List
from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
	def __init__(self):
		self.movies_collection: List[Movie] = []
		self.users_collection: List[User] = []
	
	def __get_user_by_username(self, username):
		for user in self.users_collection:
			if user.username == username:
				return user
	
	@staticmethod
	def __check_if_user_owns_movie(user: User, movie: Movie):
		if user != movie.owner:
			raise Exception(f"{user.username} is not the owner of the movie {movie.title}!")
	
	def __check_if_movie_is_uploaded(self, movie: Movie):
		if movie not in self.movies_collection:
			raise Exception(f"The movie {movie.title} is not uploaded!")
	
	def register_user(self, username: str, age: int):
		if self.__get_user_by_username(username):
			raise Exception("User already exists!")
		
		user = User(username, age)
		self.users_collection.append(user)
		return f"{username} registered successfully."
	
	def upload_movie(self, username: str, movie: Movie):
		user_who_wants_to_upload = self.__get_user_by_username(username)
		
		if movie in self.movies_collection:
			raise Exception("Movie already added to the collection!")
		
		elif not user_who_wants_to_upload:
			raise Exception("This user does not exist!")
		
		self.__check_if_user_owns_movie(user_who_wants_to_upload, movie)
		
		user_who_wants_to_upload.movies_owned.append(movie)
		self.movies_collection.append(movie)
		return f"{username} successfully added {movie.title} movie."
	
	@staticmethod
	def __edit_movie_attributes(movie, **kwargs):
		for attribute, value in kwargs.items():
			setattr(movie, attribute, value)
	
	def edit_movie(self, username: str, movie: Movie, **kwargs):
		user_who_wants_to_edit = self.__get_user_by_username(username)
		
		self.__check_if_user_owns_movie(user_who_wants_to_edit, movie)
		self.__check_if_movie_is_uploaded(movie)
		
		self.__edit_movie_attributes(movie, **kwargs)
		return f"{username} successfully edited {movie.title} movie."
	
	def delete_movie(self, username: str, movie: Movie):
		user_who_wants_to_delete = self.__get_user_by_username(username)
		
		self.__check_if_user_owns_movie(user_who_wants_to_delete, movie)
		self.__check_if_movie_is_uploaded(movie)
		
		self.movies_collection.remove(movie)
		user_who_wants_to_delete.movies_owned.remove(movie)
		
		return f"{username} successfully deleted {movie.title} movie."
	
	def like_movie(self, username: str, movie: Movie):
		user = self.__get_user_by_username(username)
		
		if movie in user.movies_liked:
			raise Exception(f"{username} already liked the movie {movie.title}!")
		
		elif movie in user.movies_owned:
			raise Exception(f"{username} is the owner of the movie {movie.title}!")
		
		movie.likes += 1
		user.movies_liked.append(movie)
		return f"{username} liked {movie.title} movie."
	
	def dislike_movie(self, username: str, movie: Movie):
		user = self.__get_user_by_username(username)
		
		if movie not in user.movies_liked:
			raise Exception(f"{username} has not liked the movie {movie.title}!")
		
		movie.likes -= 1
		user.movies_liked.remove(movie)
		return f"{username} disliked {movie.title} movie."
	
	def display_movies(self):
		sorted_movies = sorted(self.movies_collection, key=lambda x: (-x.year, x.title))
		result = '\n'.join([movie.details() for movie in sorted_movies]) if sorted_movies else "No movies found."
		
		return result
	
	def __str__(self):
		result = f"All users: {', '.join([user.username for user in self.users_collection]) if self.users_collection else 'No users.'}"
		
		result += f"\nAll movies: {', '.join([movie.title for movie in self.movies_collection]) if self.movies_collection else 'No movies.'}"
		
		return result
