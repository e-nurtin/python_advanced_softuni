from pokemon import Pokemon


class Trainer:
	def __init__(self, name: str):
		self.name = name
		self.pokemons = []
	
	def add_pokemon(self, pokemon: Pokemon):
		if pokemon not in self.pokemons:
			self.pokemons.append(pokemon)
			return f"Caught {pokemon.name} with health {pokemon.health}"
		
		return "This pokemon is already caught"
	
	def release_pokemon(self, pokemon_name: str):
		for pokem in self.pokemons:
			if pokemon_name == pokem.name:
				self.pokemons.remove(pokem)
				return f"You have released {pokemon_name}"
		
		return "Pokemon is not caught"
	
	def trainer_data(self):
		result = [f"Pokemon Trainer {self.name}",
		          f"Pokemon count {len(self.pokemons)}",
		          ]
		for pokemon in self.pokemons:
			result.append(f"- {pokemon.pokemon_details()}")
			
		return '\n'.join(result)
	
