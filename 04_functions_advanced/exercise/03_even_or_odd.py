def even_odd(*args):
	if args[-1] == 'even':
		digits = [int(x) for x in args[:-1] if int(x) % 2 == 0]
	else:
		digits = [int(x) for x in args[:-1] if int(x) % 2 != 0]
		
	return digits
