def naughty_or_nice_list(kids, *args, **kwargs):
	naughty_kids, nice_kids, not_found_kids = [], [], []
	
	for number, kid in kids:
		for arg in args:
			number, type_of_kid = [int(x) if x.isdigit() else x for x in arg.split('-')]
			