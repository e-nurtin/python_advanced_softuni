def shopping_list(budget, **kwargs):
	if not budget >= 100:
		return "You do not have enough budget."
	
	result = []
	
	for product, info in kwargs.items():
		product_cost = float(info[0]) * float(info[1])
		
		if product_cost <= budget:
			budget -= product_cost
			result.append(f"You bought {product} for {product_cost:.2f} leva.")
			
			if len(result) == 5:
				break
	
	return "\n".join(result)

