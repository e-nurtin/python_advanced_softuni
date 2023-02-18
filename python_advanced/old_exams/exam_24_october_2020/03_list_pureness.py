from collections import deque


def best_list_pureness(numbers, rotations):
	numbers = deque(numbers)
	data = {0: sum(num * i for i, num in enumerate(numbers))}
	
	max_pureness = float('-inf')
	best_rotation = 0
	
	for rotation in range(1, rotations + 1):
		numbers.appendleft(numbers.pop())
		data[rotation] = data.get(rotation, sum(num * i for i, num in enumerate(numbers)))
	
	for rotation, value in data.items():
		if max_pureness < value:
			max_pureness = value
			best_rotation = rotation
	
	return f"Best pureness {max_pureness} after {best_rotation} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)
test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)
test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
