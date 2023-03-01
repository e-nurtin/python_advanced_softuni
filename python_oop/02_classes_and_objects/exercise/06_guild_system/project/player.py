class Player:
	def __init__(self, name, hp, mp):
		self.name = name
		self.hp = hp
		self.mp = mp
		self.skills = dict()
		self.guild = "Unaffiliated"
		
	def add_skill(self, skill_name, mana_cost):
		if skill_name in self.skills:
			return "Skill already added"
		
		self.skills[skill_name] = mana_cost
		return f"Skill {skill_name} added to the collection of the player {self.name}"
	
	def player_info(self):
		details = [f"Name: {self.name}", f"Guild: {self.guild}", f"HP: {self.hp}", f"MP: {self.mp}"]
		
		for skill_name, mana_cost in self.skills.items():
			details.append(f"==={skill_name} - {mana_cost}")
		return "\n".join(details)
