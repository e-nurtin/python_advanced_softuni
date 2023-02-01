def naughty_or_nice_list(kids, *args, **kwargs):
	kids_sorted = {
		"Nice": [],
		"Naughty": [],
		"Not found": [],
	}
	
	data_numbers = {}
	data_names = {}
	
	for number, name in kids:
		if number not in data_numbers:
			data_numbers[number] = []
		data_numbers[number].append(name)
	
	for arg in args:
		digit, type_of_kid = [int(x) if x.isdigit() else x for x in arg.split("-")]
		
		if digit in data_numbers:
			if len(data_numbers[digit]) == 1:
				kids_sorted[type_of_kid].append(data_numbers[digit][0])
				kids.remove((digit, data_numbers[digit][0]))
	
	if kwargs:
		for number, name in kids:
			if name not in data_names:
				data_names[name] = [0, ]
			data_names[name][0] += 1
			data_names[name].append(number)
		
		for name, type_of_kid in kwargs.items():
			if name in data_names:
				if data_names[name][0] == 1:
					kids_sorted[type_of_kid].append(name)
					kids.remove((data_names[name][-1], name))
					
	for kid in kids:
		kids_sorted["Not found"].append(kid[1])
	
	result = []
	for type_of_kid, kids in kids_sorted.items():
		if kids:
			result.append(f"{type_of_kid}: {', '.join(kids)}")
	
	return '\n'.join(result)


print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))

