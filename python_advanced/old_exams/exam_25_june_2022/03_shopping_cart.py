def shopping_cart(*args):
	shopping_list = {
		"Soup": [],
		"Pizza": [],
		"Dessert": [],
	}
	
	max_products = {
		"Soup": 3,
		"Pizza": 4,
		"Dessert": 2,
	}
	
	for arg in args:
		if arg == "Stop":
			break
			
		meal, ingredient = arg[0], arg[1]
		
		if meal not in shopping_list:
			shopping_list[meal] = []
		
		if max_products[meal] > len(shopping_list[meal]) and ingredient not in shopping_list[meal]:
			shopping_list[meal].append(ingredient)
			
	if all([len(x[1]) == 0 for x in shopping_list.items()]):
		return "No products in the cart!"
	
	result = []
	for meal, ingredients in sorted(shopping_list.items(), key= lambda x: (-len(x[1]), x[0])):
		result.append(f"{meal}:")
		for ingredient in sorted(ingredients):
			result.append(f" - {ingredient}")
			
	return '\n'.join(result)
