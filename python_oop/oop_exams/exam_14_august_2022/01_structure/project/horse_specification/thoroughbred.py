from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
	MAX_SPEED = 140
	
	def train(self):
		trained_speed = self.speed + 3
		if trained_speed > self.MAX_SPEED:
			self.speed = self.MAX_SPEED