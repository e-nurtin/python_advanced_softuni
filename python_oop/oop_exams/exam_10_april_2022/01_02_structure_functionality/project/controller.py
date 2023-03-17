from collections import deque
from typing import List
from project.player import Player
from project.supply.supply import Supply


class Controller:
	def __init__(self):
		self.players: List[Player] = []
		self.supplies: List[Supply] = []
	
	@property
	def sustenance_types(self):
		return ['Food', 'Drink']
	
	def __remove_supply(self, supply):
		self.supplies.reverse()
		self.supplies.remove(supply)
		self.supplies.reverse()
		
	def __adjust_player_stamina(self, supply, player):
		if player.stamina + supply.energy > 100:
			player.stamina = 100
		else:
			player.stamina += supply.energy
		
		self.__remove_supply(supply)
		return f"{player.name} sustained successfully with {supply.name}."
	
	def __check_if_there_is_supply(self, sustenance_type, player):
		for supply in reversed(self.supplies):
			if type(supply).__name__ == sustenance_type:
				return self.__adjust_player_stamina(supply, player)
		
		raise Exception(f"There are no {sustenance_type.lower()} supplies left!")
	
	@staticmethod
	def __check_for_zero_stamina(*players):
		result = []
		for player in players:
			if player.stamina == 0:
				result.append(f"Player {player.name} does not have enough stamina.")
		return result
	
	def __get_player_by_name(self, player_name):
		for player in self.players:
			if player.name == player_name:
				return player
	
	def add_player(self, *players):
		added_names = []
		for player in players:
			if self.__get_player_by_name(player.name):
				continue
				
			added_names.append(player.name)
			self.players.append(player)
		
		return f"Successfully added: {', '.join(added_names)}"
	
	def add_supply(self, *supplies):
		for supply in supplies:
			self.supplies.append(supply)
	
	def sustain(self, player_name: str, sustenance_type: str):
		player = self.__get_player_by_name(player_name)
		
		if not player or sustenance_type not in self.sustenance_types:
			return
		
		elif not player.need_sustenance:
			return f"{player_name} have enough stamina."
		
		return self.__check_if_there_is_supply(sustenance_type, player)
	
	def duel(self, first_player_name: str, second_player_name: str):
		first_player = self.__get_player_by_name(first_player_name)
		second_player = self.__get_player_by_name(second_player_name)
		
		players_with_zero_stamina = self.__check_for_zero_stamina(first_player, second_player)
		if players_with_zero_stamina:
			return '\n'.join(players_with_zero_stamina)
		
		return self.__begin_duel(first_player, second_player)
	
	@staticmethod
	def __begin_duel(*players):
		players = deque(sorted(players, key=lambda p: p.stamina))
		
		for _ in range(len(players)):
			attacker = players.popleft()
			attacked_player = players[0]
			
			players.append(attacker)
			attacker_damage = attacker.stamina * 0.5
			
			if attacked_player.stamina - attacker_damage <= 0:
				attacked_player.stamina = 0
				break
			
			attacked_player.stamina -= attacker_damage
			
		winner = list(sorted(players, key=lambda p: -p.stamina))[0]
		return f"Winner: {winner.name}"

	def next_day(self):
		for player in self.players:
			
			if player.stamina - player.age * 2 < 0:
				player.stamina = 0
			else:
				player.stamina -= player.age * 2
			
			for food_type in self.sustenance_types:
				self.sustain(player.name, food_type)
			
	def __str__(self):
		result = [str(p) for p in self.players]
		result.extend([s.details() for s in self.supplies])
		
		return '\n'.join(result)