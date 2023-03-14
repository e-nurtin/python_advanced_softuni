from project.horse_specification.horse import Horse


class Appaloosa(Horse):
	MAX_SPEED = 120
	
	def train(self):
		trained_speed = self.speed + 2
		if trained_speed > self.MAX_SPEED:
			self.speed = self.MAX_SPEED
