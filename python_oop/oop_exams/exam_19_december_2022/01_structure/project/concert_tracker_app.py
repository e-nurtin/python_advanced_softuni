from typing import List
from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
	VALID_MUSICIAN_TYPES = {"Guitarist": Guitarist, "Drummer": Drummer, "Singer": Singer}
	CONCERT_GENRES = []
	
	def __init__(self):
		self.bands: List[Band] = []
		self.musicians: List[Musician] = []
		self.concerts: List[Concert] = []
	
	@staticmethod
	def find_from_name(entities, entity_name):
		for entity in entities:
			if entity.name == entity_name:
				return entity
	
	@staticmethod
	def check_for_each_type_of_musician(band: Band):
		for musician_type in ConcertTrackerApp.VALID_MUSICIAN_TYPES:
			if not any([True for musician in band.members if musician.__class__.__name__ == musician_type]):
				return False
		return True
	
	@staticmethod
	def check_if_band_can_play_concert(concert_genre: str, band: Band):
		skills_needed = Concert.AVAILABLE_GENRES_SKILLS_NEEDED[concert_genre]
		
		for member in band.members:
			if not all([skill for skill in skills_needed[member.__class__.__name__] if skill in member.skills]):
				return False
		
		return True
	
	def create_musician(self, musician_type: str, name: str, age: int):
		
		if musician_type not in ConcertTrackerApp.VALID_MUSICIAN_TYPES:
			raise ValueError("Invalid musician type!")
		
		elif self.find_from_name(self.musicians, name):
			raise Exception(f"{name} is already a musician!")
		
		self.musicians.append(ConcertTrackerApp.VALID_MUSICIAN_TYPES[musician_type].from_name(name, age))
		return f"{name} is now a {musician_type}."
	
	def create_band(self, name: str):
		if self.find_from_name(self.bands, name):
			raise f"{name} band is already created!"
		
		self.bands.append(Band.from_name(name))
		return f"{name} was created."
	
	def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
		concert = [c for c in self.concerts if c.place == place]
		if concert:
			raise Exception(f"{place} is already registered for {concert[0].genre} concert!")
		
		self.concerts.append(Concert(genre, audience, ticket_price, expenses, place))
		return f"{genre} concert in {place} was added."
	
	def add_musician_to_band(self, musician_name: str, band_name: str):
		musician = self.find_from_name(self.musicians, musician_name)
		band = self.find_from_name(self.bands, band_name)
		
		if not musician:
			raise Exception(f"{musician_name} isn't a musician!")
		
		elif not band:
			raise Exception(f"{band_name} isn't a band!")
		
		band.add_member(musician)
		return f"{musician_name} was added to {band_name}."
	
	def remove_musician_from_band(self, musician_name: str, band_name: str):
		band = self.find_from_name(self.bands, band_name)
		musician = self.find_from_name(self.musicians, musician_name)
		
		if not band:
			raise Exception(f"{band_name} isn't a band!")
		
		elif not musician:
			raise Exception(f"{musician_name} isn't a member of {band_name}!")
		
		band.remove_member(musician)
		return f"{musician_name} was removed from {band_name}."
	
	def start_concert(self, concert_place: str, band_name: str):
		
		band = self.find_from_name(self.bands, band_name)
		concert = [concert for concert in self.concerts if concert_place == concert.place][0]
		
		if not self.check_for_each_type_of_musician(band):
			raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")
		
		elif not self.check_if_band_can_play_concert(concert.genre, band):
			raise Exception(f"The {band_name} band is not ready to play at the concert!")
		
		profit = (concert.audience * concert.ticket_price) - concert.expenses
		return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."
	