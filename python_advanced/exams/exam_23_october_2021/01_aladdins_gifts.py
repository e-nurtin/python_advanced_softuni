from collections import deque

materials = deque([int(x) for x in input().split()])
magic_levels = deque([int(x) for x in input().split()])

succesful_craft = {'Gemstone', 'Porcelain Sculpture'}
crafted_gifts = {}

while materials and magic_levels:
	material_ = materials.pop()
	magic_level_ = magic_levels.popleft()
	current_sum = material_ + magic_level_
	
	if current_sum < 100:
		
		if current_sum % 2 == 0:
			current_sum = (material_ * 2) + (magic_level_ * 3)
		else:
			current_sum *= 2
			
	elif current_sum > 499:
		current_sum /= 2
	
	if 100 <= current_sum <= 199:
		crafted_gifts['Gemstone'] = crafted_gifts.get('Gemstone', 0) + 1
		
	elif 200 <= current_sum <= 299:
		crafted_gifts['Porcelain Sculpture'] = crafted_gifts.get('Porcelain Sculpture', 0) + 1
		
	elif 300 <= current_sum <= 399:
		crafted_gifts['Gold'] = crafted_gifts.get('Gold', 0) + 1
		
	elif 400 <= current_sum <= 499:
		crafted_gifts['Diamond Jewellery'] = crafted_gifts.get('Diamond Jewellery', 0) + 1
	
if {'Gemstone', 'Porcelain Sculpture'}.issubset(set(crafted_gifts.keys())) or \
		{'Gold', 'Diamond Jewellery'}.issubset(set(crafted_gifts.keys())):
	
	print("The wedding presents are made!")
else:
	print("Aladdin does not have enough wedding presents.")

if materials:
	print(f"Materials left: {', '.join([str(x) for x in materials])}")
if magic_levels:
	print(f"Magic left: {', '.join([str(x) for x in magic_levels])}")
	
[print(f"{key}: {value}") for key, value in sorted(crafted_gifts.items())]
