numbers_to_check = list(map(int, input().split()))
target_number = int(input())

targets = set()
values = {}

for number in numbers_to_check:
	if number in targets:
		targets.remove(number)
		pair = values[number]
		del values[number]
		print(f"{pair} + {number} = {target_number}")
	else:
		difference = target_number - number
		targets.add(difference)
		values[difference] = number

# from _collections import deque
#
# # numbers_to_check = deque(list(map(int, input().split())))
# # target_number = int(input())
# # index = 0
# #
# # while True:
# # 	current_number = numbers_to_check.popleft()
# #
# # 	if current_number <= target_number:
# # 		for number in numbers_to_check:
# # 			if current_number + number == target_number:
# # 				numbers_to_check.remove(number)
# # 				print(f"{current_number} + {number} = {target_number}")
# # 				index = 0
# # 				break
# # 		else:
# # 			numbers_to_check.append(current_number)
# #
# # 	index += 1
# # 	if index == len(numbers_to_check):
# # 		break
