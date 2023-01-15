from collections import deque

cups = deque([int(x) for x in input().split()])
bottles = deque([int(x) for x in input().split()])

wasted_water = 0

current_cup = cups.popleft()

while True:
	
	current_bottle = bottles.pop()
	current_cup -= current_bottle
	
	if current_cup <= 0:
		wasted_water += abs(current_cup)
		if not bottles:
			cups = ' '.join([str(x) for x in cups])
			print(f"Cups: {cups}")
			break
			
		elif cups:
			current_cup = cups.popleft()
			
		else:
			bottles = ' '.join(sorted([str(x) for x in bottles], reverse=True))
			print(f"Bottles: {bottles}")
			break
	
print(f"Wasted litters of water: {wasted_water}")
