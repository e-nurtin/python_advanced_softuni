from project import FormulaTeam


class MercedesTeam(FormulaTeam):
	EXPENSES_PER_RACE = 200_000
	SPONSORS = {
		'Petronas': {1: 1_000_000, 2: 500_000},
		'TeamViewer': {5: 100_000, 7: 50_000},
	}
	
	def __init__(self, budget: int):
		super().__init__(budget)
	
	@classmethod
	def from_budget(cls, budget: int) -> 'MercedesTeam':
		return cls(budget)
	
	@staticmethod
	def get_revenue(race_position: int):
		revenue = 0
		for sponsor, values in MercedesTeam.SPONSORS.items():
			for pos, value in values.items():
				if race_position <= pos:
					revenue += value
					break
		return revenue
	
	def calculate_revenue_after_race(self, race_pos: int):
		revenue = self.get_revenue(race_pos)
		revenue -= MercedesTeam.EXPENSES_PER_RACE
		
		self.budget += revenue
		return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
