def sorting_cheeses(**kwargs):
	to_print = ''
	
	for cheese, values in sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0])):
		to_print += cheese + "\n"
		# to_print += '\n'.join([str(x) for x in sorted(values, reverse=True)]) + "\n"
		to_print += '\n'.join(map(str, sorted(values, reverse=True))) + "\n"
		# for value in sorted(values, key=lambda x: (-x)):
		# 	to_print += f"{value}\n"

	return to_print


print(sorting_cheeses(
	Parmesan=[102, 120, 135],
	Camembert=[100, 100, 105, 500, 430],
	Mozzarella=[50, 125],
)
)
print(
	sorting_cheeses(
		Parmigiano=[165, 215],
		Feta=[150, 515],
		Brie=[150, 125]
	)
)
