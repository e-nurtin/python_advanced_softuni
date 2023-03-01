class Guild:
	def __init__(self, name):
		self.name = name
		self.players = []
		
	def assign_player(self, player):
		if player.guild == self.name:
			return f"Player {player.name} is already in the guild."
		
		elif player.guild == 'Unaffiliated':
			self.players.append(player)
			player.guild = self.name
			return f"Welcome player {player.name} to the guild {self.name}"
		
		else:
			return f"Player {player.name} is in another guild."
	
	def kick_player(self, player_name: str):
		try:
			player = next(filter(lambda p: p.name == player_name, self.players))
			player.guild = 'Unaffiliated'
			return f"Player {player_name} has been removed from the guild."
		
		except StopIteration:
			return f"Player {player_name} is not in the guild."
		# for player in self.players:
		#
		# 	if player.name == player_name:
		# 		player.guild = "Unaffiliated"
		# 		self.players.remove(player)
		# 		return f"Player {player_name} has been removed from the guild."
		# return f"Player {player_name} is not in the guild."
		
	def guild_info(self):
		info = [f"Guild: {self.name}"]
		for player in self.players:
			info.append(player.player_info())
		
		return "\n".join(info)
