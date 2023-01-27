from collections import deque

caffeine_list = deque([int(x) for x in input().split(', ')])
energy_drinks = deque([int(x) for x in input().split(', ')])
caffeine_intake = 0

while caffeine_list and energy_drinks:
	caffeine = caffeine_list.pop()
	drink = energy_drinks.popleft()
	
	total_caffeine = caffeine * drink
	
	if caffeine_intake + total_caffeine > 300:
		energy_drinks.append(drink)
		
		if caffeine_intake >= 30:
			caffeine_intake -= 30
			
		else:
			caffeine_intake = 0
			
		continue
	
	caffeine_intake += total_caffeine
		
if energy_drinks:
	print(f"Drinks left: {', '.join([str(drink) for drink in energy_drinks])}")
else:
	print(f"At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {caffeine_intake} mg caffeine.")