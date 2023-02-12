def add_to_list(list_to_add, info, *args):
	result = []
	if info == 'beginning':
		result = list(args)
		result.extend(list_to_add)
	elif info == 'end':
		result.extend(list_to_add)
		result.extend(args)
	
	return result


def remove_from_list(list_of_numbers, info, *args):
	if info == 'beginning':
		if args:
			to_remove = int(args[0])
			list_of_numbers = list_of_numbers[to_remove:]
		else:
			list_of_numbers = list_of_numbers[1:]
			
	elif info == 'end':
		if args:
			to_remove = int(args[0])
			list_of_numbers = list_of_numbers[:-1 * to_remove]
		else:
			list_of_numbers.pop()
	
	return list_of_numbers


def list_manipulator(list_of_numbers, action, info, *args):
	if action == 'add':
		list_of_numbers = add_to_list(list_of_numbers, info, *args)
	elif action == 'remove':
		list_of_numbers = remove_from_list(list_of_numbers, info, *args)
	
	return list_of_numbers


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
