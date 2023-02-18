def delivery_of_flavors(inventory, *args):
	for arg in args:
		inventory.append(arg)
	return inventory


def sell_flavors(inventory, *args):
	new_inventory = []
	if not args:
		return inventory[1:]
	
	if isinstance(args[0], int):
		new_inventory = inventory[int(args[0]):]

	else:
		for item in inventory:
			if item not in args:
				new_inventory.append(item)
	return new_inventory


def stock_availability(inventory, action, *args):
	possible_actions = {
		'delivery': delivery_of_flavors,
		'sell': sell_flavors,
	}
	
	inventory = possible_actions[action](inventory, *args)
	
	return inventory
