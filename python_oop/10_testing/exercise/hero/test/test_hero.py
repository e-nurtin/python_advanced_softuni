from project.hero import Hero
from unittest import TestCase, main


class HeroTest(TestCase):
	def test_hero_init_username_available(self):
		hero = Hero('user', 1, 80.2, 20.5)
		
		self.assertEqual('user', hero.username)
	
	def test_hero_init_level_available(self):
		hero = Hero('user', 1, 80.2, 20.5)
		
		self.assertEqual(1, hero.level)
	
	def test_hero_init_health_available(self):
		hero = Hero('user', 1, 80.2, 20.5)
		
		self.assertEqual(80.2, hero.health)
	
	def test_hero_init_damage_available(self):
		hero = Hero('user', 1, 80.2, 20.5)
		
		self.assertEqual(20.5, hero.damage)
	
	def test_battle_method_same_name_enemy_raises(self):
		hero = Hero('user', 1, 80.2, 20.5)
		enemy_hero = Hero('user', 1, 80.2, 22.5)
		
		with self.assertRaises(Exception) as exc:
			hero.battle(enemy_hero)
		
		self.assertEqual("You cannot fight yourself", str(exc.exception))
	
	def test_battle_method_self_health_zero_raises(self):
		hero = Hero('user', 1, 0, 20.5)
		enemy_hero = Hero('user_other', 1, 80.2, 22.5)
		
		with self.assertRaises(ValueError) as exc:
			hero.battle(enemy_hero)
		
		self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(exc.exception))
	
	def test_battle_method_self_health_negative_raises(self):
		hero = Hero('user', 1, -20, 20.5)
		enemy_hero = Hero('user_other', 1, 80.2, 22.5)
		
		with self.assertRaises(ValueError) as exc:
			hero.battle(enemy_hero)
		
		self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(exc.exception))
	
	def test_battle_method_enemy_health_zero_raises(self):
		hero = Hero('user', 1, 100, 20.5)
		enemy_hero = Hero('user_other', 1, 0, 22.5)
		
		with self.assertRaises(ValueError) as exc:
			hero.battle(enemy_hero)
		
		self.assertEqual("You cannot fight user_other. He needs to rest", str(exc.exception))
	
	def test_battle_method_enemy_health_negative_raises(self):
		hero = Hero('user', 1, 100, 20.5)
		enemy_hero = Hero('user_other', 1, -520, 22.5)
		
		with self.assertRaises(ValueError) as exc:
			hero.battle(enemy_hero)
		
		self.assertEqual("You cannot fight user_other. He needs to rest", str(exc.exception))
	
	def test_battle_method_if_equal_draw_returns(self):
		hero = Hero('user', 1, 22.5, 20.5)
		enemy_hero = Hero('user_other', 1, 20.5, 22.5)
		
		result = hero.battle(enemy_hero)
		expected = "Draw"
		
		self.assertEqual(expected, result)
	
	def test_battle_method_if_negative_draw_returns(self):
		hero = Hero('user', 1, 22.5, 100)
		enemy_hero = Hero('user_other', 1, 20.5, 200.5)
		
		result = hero.battle(enemy_hero)
		expected = "Draw"
		
		self.assertEqual(expected, result)
	
	def test_battle_method_if_self_is_winner_returns(self):
		hero = Hero('user', 1, 100.5, 100)
		enemy_hero = Hero('user_other', 1, 20.5, 20.5)
		
		result = hero.battle(enemy_hero)
		expected = "You win"
		
		self.assertEqual(expected, result)
	
	def test_battle_method_if_self_winner_level_increments(self):
		hero = Hero('user', 1, 100.5, 100)
		enemy_hero = Hero('user_other', 1, 20.5, 20.5)
		
		self.assertEqual(1, hero.level)
		hero.battle(enemy_hero)
		
		self.assertEqual(2, hero.level)
	
	def test_battle_method_if_self_winner_health_increments(self):
		hero = Hero('user', 1, 100.5, 100)
		enemy_hero = Hero('user_other', 1, 20.5, 20.5)
		
		self.assertEqual(100.5, hero.health)
		hero.battle(enemy_hero)
		
		self.assertEqual(85.0, hero.health)
	
	def test_battle_method_if_self_winner_damage_increments(self):
		hero = Hero('user', 1, 100.5, 100)
		enemy_hero = Hero('user_other', 1, 20.5, 20.5)
		
		self.assertEqual(100, hero.damage)
		hero.battle(enemy_hero)
		
		self.assertEqual(105, hero.damage)
	
	def test_battle_method_if_self_is_loser_returns(self):
		hero = Hero('user', 1, 20.5, 20)
		enemy_hero = Hero('user_other', 1, 200.5, 20.5)
		
		result = hero.battle(enemy_hero)
		expected = "You lose"
		
		self.assertEqual(expected, result)
	
	def test_battle_method_when_enemy_wins_their_health_increments(self):
		hero = Hero('user', 1, 50, 20)
		enemy_hero = Hero('user_other', 1, 200, 60)
		
		self.assertEqual(200, enemy_hero.health)
		hero.battle(enemy_hero)
		
		self.assertEqual(185, enemy_hero.health)
	
	def test_battle_method_when_enemy_wins_their_level_increments(self):
		hero = Hero('user', 1, 50, 20)
		enemy_hero = Hero('user_other', 1, 200, 60)
		
		self.assertEqual(1, enemy_hero.level)
		hero.battle(enemy_hero)
		
		self.assertEqual(2, enemy_hero.level)
	
	def test_battle_method_when_enemy_wins_their_damage_increments(self):
		hero = Hero('user', 1, 50, 20)
		enemy_hero = Hero('user_other', 1, 200, 60)
		
		self.assertEqual(60, enemy_hero.damage)
		hero.battle(enemy_hero)
		
		self.assertEqual(65, enemy_hero.damage)
	
	def test_continuous_battle(self):
		hero = Hero('user', 1, 700, 50)
		enemy_hero = Hero('user_other', 1, 200, 50)
		
		hero.battle(enemy_hero)
		
		self.assertEqual(55, enemy_hero.damage)
		self.assertEqual(650, hero.health)
		self.assertEqual(155, enemy_hero.health)
		
		result = hero.battle(enemy_hero)
		
		self.assertEqual(3, enemy_hero.level)
		self.assertEqual('You lose', result)
		
		hero.battle(enemy_hero)
		
		self.assertEqual(360, hero.health)
		self.assertEqual(65, enemy_hero.health)
		hero.damage = 100
		
		result = hero.battle(enemy_hero)
		
		self.assertEqual('You win', result)
		self.assertEqual(2, hero.level)
		self.assertEqual(105, hero.health)
		self.assertEqual(105, hero.damage)
	
	def test_str_method_returns(self):
		hero = Hero('Enngy', 80, 700, 250)
		
		result = str(hero)
		expected = f"Hero Enngy: 80 lvl\nHealth: 700\nDamage: 250\n"
		
		self.assertEqual(expected, result)
	

if __name__ == '__main__':
	main()
