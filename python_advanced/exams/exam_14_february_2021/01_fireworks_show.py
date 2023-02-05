from collections import deque

fireworks = deque([int(x) for x in input().split(', ')])
explosives = deque([int(x) for x in input().split(', ')])

firework_data = {
	"Palm Fireworks": 0,
	"Willow Fireworks": 0,
	"Crossette Fireworks": 0,
}

while fireworks and explosives:
	
	current_firework = fireworks.popleft() if explosives[-1] > 0 or fireworks[0] <= 0 else 0
	current_explosive = explosives.pop() if current_firework > 0 or explosives[-1] <= 0 else 0

	if current_explosive <= 0:
		continue
	
	sum_of_fireworks = current_firework + current_explosive
	
	if sum_of_fireworks % 3 == 0:
		
		if sum_of_fireworks % 5 == 0:
			firework_data["Crossette Fireworks"] += 1
		
		else:
			firework_data["Palm Fireworks"] += 1
	
	elif sum_of_fireworks % 5 == 0:
		firework_data["Willow Fireworks"] += 1
	
	else:
		fireworks.append(current_firework - 1)
		explosives.append(current_explosive)
	
	if all([value >= 3 for value in firework_data.values()]):
		print("Congrats! You made the perfect firework show!")
		break

else:
	print("Sorry. You can't make the perfect firework show.")

if fireworks:
	print(f"Firework Effects left: {', '.join([str(x) for x in fireworks])}")
if explosives:
	print(f"Explosive Power left: {', '.join([str(x) for x in explosives])}")

for firework, count in firework_data.items():
	print(f"{firework}: {count}")
