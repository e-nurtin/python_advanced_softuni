from collections import deque

material_sequence = deque(list(map(int, input().split())))
magic_sequence = deque(list(map(int, input().split())))
first_combination, second_combination = {'Doll', 'Wooden train'}, {'Teddy bear', 'Bicycle'}

toys_made = {}
presents = {
	150: 'Doll',
	250: 'Wooden train',
	300: 'Teddy bear',
	400: 'Bicycle',
}

while material_sequence and magic_sequence:
	
	current_material = material_sequence.pop() if magic_sequence[0] or not material_sequence[-1] else 0
	current_magic = magic_sequence.popleft() if current_material or not magic_sequence[0] else 0
	
	if current_magic == 0:
		continue

	operation_result = current_magic * current_material
	if operation_result in presents:
		toys_made[presents[operation_result]] = toys_made.get(presents[operation_result], 0) + 1
		# if possible_toys[operation_result] not in toys_made:
		# 	toys_made[possible_toys[operation_result]] = 0
		#
		# toys_made[possible_toys[operation_result]] += 1
	
	elif operation_result < 0:
		material_sequence.append(current_magic + current_material)
		
	elif operation_result > 0:
		material_sequence.append(current_material + 15)
		
	# else:
	# 	if current_magic != 0:
	# 		magic_sequence.appendleft(current_magic)
	# 	if current_material != 0:
	# 		material_sequence.append(current_material)

if first_combination.issubset(set(toys_made.keys()))\
		or second_combination.issubset(set(toys_made.keys())):
	print("The presents are crafted! Merry Christmas!")
else:
	print("No presents this Christmas!")

if material_sequence:
	print(f"Materials left: {', '.join([str(x) for x in reversed(material_sequence)])}")
	
if magic_sequence:
	print(f"Magic left: {', '.join([str(x) for x in magic_sequence])}")


for toy, count in sorted(toys_made.items()):
	print(f"{toy}: {count}")
