def grocery_store(**products):
	
	products = list(sorted(products.items(), key=lambda x: (-x[1], -len(x[0]), x[0])))
	
	result = [f"{n}: {q}" for n, q in products]
	
	# for name, quantity in products:
	# 	result.append(f"{name}: {quantity}")
	#
	return '\n'.join(result)

