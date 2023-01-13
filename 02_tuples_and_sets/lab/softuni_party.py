count_of_guests = int(input())

guest_data = {
	'vip': [],
	'regular': [],
}

for _ in range(count_of_guests):
	current_guest = input()
	
	if current_guest[0].isdigit():
		pass
	


# count_of_guests = int(input())
#
# vip_guests = []
# regular_guests = []
#
# for _ in range(count_of_guests):
# 	current_guest = input()
#
# 	if current_guest[0].isdigit():
# 		vip_guests.append(current_guest)
# 	else:
# 		regular_guests.append(current_guest)
#
# vip_guests, regular_guests = set(vip_guests), set(regular_guests)
#
# arrived_guest = input()
# while arrived_guest != "END":
# 	if arrived_guest in vip_guests:
# 		vip_guests.remove(arrived_guest)
# 	elif arrived_guest in regular_guests:
# 		regular_guests.remove(arrived_guest)
# 	arrived_guest = input()
#
#
# print(len(vip_guests)+len(regular_guests))
# if vip_guests:
# 	print('\n'.join(sorted(vip_guests)))
# if regular_guests:
# 	print('\n'.join(sorted(regular_guests)))
