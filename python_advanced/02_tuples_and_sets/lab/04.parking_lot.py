def print_func(parked_cars):
	if parked_cars:
		print('\n'.join(set(parking_lot)))
	else:
		print("Parking Lot is Empty")


number_of_cars = int(input())

parking_lot = set()

data_process = {
	'IN': lambda x: parking_lot.add(x),
	'OUT': lambda x: parking_lot.remove(x),
}

for _ in range(number_of_cars):
	action, license_plate = input().split(', ')
	
	data_process[action](license_plate)

print_func(parking_lot)
	