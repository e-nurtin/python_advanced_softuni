def add_to_list(list_to_add, info, *args):
	if info == 'beginning':
		[list_to_add.insert(0, num) for num in args]
	
	elif info == 'end':
		list_to_add.extend(args)
	
	return list_to_add


def remove_from_list(list_of_numbers, info, *args):
	to_remove = int(args[0]) if args else 1
	
	if info == 'beginning':
		list_of_numbers = list_of_numbers[to_remove:]
	
	elif info == 'end':
		list_of_numbers = list_of_numbers[:-to_remove]
	
	return list_of_numbers


def list_manipulator(list_of_numbers, action, info, *args):
	if action == 'add':
		list_of_numbers = add_to_list(list_of_numbers, info, *args)
	
	elif action == 'remove':
		list_of_numbers = remove_from_list(list_of_numbers, info, *args)
	
	return list_of_numbers

