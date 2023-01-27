# # 2
guests = set(input() for guest in range(int(input())))
arrived_guests = set()

current_guest = input()
while current_guest != "END":
	
	arrived_guests.add(current_guest)
	current_guest = input()
	
# Both of the below methods yield the same result. On one of them method name is used and on the other operators.

# guests_missing = guests - arrived_guests
guests_missing = set(guests).difference(arrived_guests)
#

print(len(guests_missing))
print('\n'.join(sorted(guests_missing)))

# # 1
# vip_guests = set()
# regular_guests = set()
#
# for _ in range(count_of_guests):
# 	current_guest = input()
#
# 	if current_guest[0].isdigit():
# 		vip_guests.add(current_guest)
# 	else:
# 		regular_guests.add(current_guest)

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
