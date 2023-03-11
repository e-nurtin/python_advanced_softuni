from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
	EXPENSES_PER_RACE = 250_000
	SPONSORS = {
		'Oracle': {1: 1_500_000, 2: 800_000},
		'Honda': {8: 20_000, 10: 10_000},
	}
	
	def __init__(self, budget: int):
		super().__init__(budget)
	
	@staticmethod
	def get_revenue(position: int):
		revenue = 0
		for sponsor, values in RedBullTeam.SPONSORS.items():
			for pos, value in values.items():
				if position <= pos:
					revenue += value
					break
		return revenue
		
	def calculate_revenue_after_race(self, race_pos: int):
		revenue = self.get_revenue(race_pos)
		revenue -= RedBullTeam.EXPENSES_PER_RACE
		self.budget += revenue
		
		return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
