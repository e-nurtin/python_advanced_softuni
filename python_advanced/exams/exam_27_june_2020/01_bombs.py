from collections import deque


def check_if_bag_full(bombs):
	if all([bomb >= 3 for bomb in bombs.values()]):
		return True
	return False


bomb_data = {
	40: 'Datura Bombs',
	60: 'Cherry Bombs',
	120: 'Smoke Decoy Bombs',
}

bag_is_full = False

bombs_made = {}
bomb_effects = deque(list(map(int, input().split(', '))))
bomb_casings = deque(list(map(int, input().split(', '))))

for bomb in bomb_data.values():
	bombs_made[bomb] = 0

while bomb_effects and bomb_casings:
	current_effect = bomb_effects.popleft()
	current_casing = bomb_casings.pop()
	
	while True:
		current_sum = current_casing + current_effect
		
		if current_sum in bomb_data:
			bombs_made[bomb_data[current_sum]] = bombs_made.get(bomb_data[current_sum], 0) + 1
			bag_is_full = check_if_bag_full(bombs_made)
			break
		
		current_casing -= 5
	
	if bag_is_full:
		break

if not bag_is_full:
	print("You don't have enough materials to fill the bomb pouch.")
else:
	print("Bene! You have successfully filled the bomb pouch!")


if bomb_effects:
	print(f"Bomb Effects: {', '.join([str(x) for x in bomb_effects])}")
else:
	print(f"Bomb Effects: empty")

if bomb_casings:
	print(f"Bomb Casings: {', '.join([str(x) for x in bomb_casings])}")
else:
	print(f"Bomb Casings: empty")

# print(f"Bomb Effects: {'empty' if not bomb_effects else ', '.join([str(x) for x in bomb_effects])}")
# print(f"Bomb Casings: {'empty' if not bomb_effects else ', '.join([str(x) for x in bomb_casings])}")

for name, count in sorted(bombs_made.items()):
	print(f"{name}: {count}")
