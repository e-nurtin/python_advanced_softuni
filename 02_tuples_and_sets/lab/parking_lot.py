number_of_cars = int(input())

parking_lot = []

data_process = {
	'IN': lambda x: parking_lot.append(x),
	'OUT': lambda x: parking_lot.remove(x),
}

for _ in range(number_of_cars):
	action, license_plate = input().split(', ')
	
	data_process[action](license_plate)

if parking_lot:
	print('\n'.join(set(parking_lot)))
else:
	print("Parking Lot is Empty")
	