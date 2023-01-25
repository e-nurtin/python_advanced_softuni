def negative_positive(*args):
	positive = sum([int(x) if int(x) > 0 else 0 for x in args[0]])
	negative = sum([int(x) if int(x) < 0 else 0 for x in args[0]])
	
	if abs(negative) > positive:
		stronger = 'negatives'
		weaker = 'positives'
	else:
		stronger = 'positives'
		weaker = 'negatives'
	
	return f"{negative}\n" \
			f"{positive}\n" \
	        f"The {stronger} are stronger than the {weaker}"

