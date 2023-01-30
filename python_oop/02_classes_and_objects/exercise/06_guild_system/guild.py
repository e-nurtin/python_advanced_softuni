from player import Player


class Guild:
	def __init__(self, name):
		self.name = name
		self.players = []
		self.no_guild = "Unaffiliated"
		
	def assign_player(self, player: Player):
		if player not in self.players and player.guild == self.no_guild:
			self.players.append(player)
			player.guild = self.name
			return f"Welcome player {player.name} to the guild {self.name}"
		
		elif player not in self.players and player.guild != self.no_guild:
			return f"Player {player.name} is in another guild."
		
		else:
			return f"Player {player.name} is already in the guild."
	
	def kick_player(self, player_name: str):
		for player in self.players:
			
			if player.name == player_name:
				player.guild = self.no_guild
				self.players.remove(player)
				return f"Player {player_name} has been removed from the guild."
		return f"Player {player_name} is not in the guild."
	
	def guild_info(self):
		info = [f"Guild: {self.name}"]
		for player in self.players:
			info.append(player.player_info())
		
		return "\n".join(info)
