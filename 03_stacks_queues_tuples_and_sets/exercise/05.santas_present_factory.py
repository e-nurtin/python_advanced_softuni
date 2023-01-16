from collections import deque

material_sequence = deque(list(map(int, input().split())))
magic_sequence = deque(list(map(int, input().split())))


toys_made = {}
possible_toys = {
	150: 'Doll',
	250: 'Wooden train',
	300: 'Teddy bear',
	400: 'Bicycle',
}

while material_sequence and magic_sequence:
	
	current_material = material_sequence.pop()
	current_magic = magic_sequence.popleft()

	operation_result = current_magic * current_material
	if operation_result in possible_toys:
		
		if possible_toys[operation_result] not in toys_made:
			toys_made[possible_toys[operation_result]] = 0
			
		toys_made[possible_toys[operation_result]] += 1
	
	elif operation_result < 0:
		operation_result = current_magic + current_material
		material_sequence.append(operation_result)
		
	elif operation_result > 0:
		current_material += 15
		material_sequence.append(current_material)
		
	else:
		if current_magic != 0:
			magic_sequence.appendleft(current_magic)
		if current_material != 0:
			material_sequence.append(current_material)

if ('Doll' in toys_made and 'Wooden train' in toys_made)\
		or ('Teddy bear' in toys_made and 'Bicycle' in toys_made):
	
	print("The presents are crafted! Merry Christmas!")
else:
	print("No presents this Christmas!")

if material_sequence:
	print(f"Materials left: {', '.join([str(x) for x in reversed(material_sequence)])}")
	
if magic_sequence:
	print(f"Magic left: {', '.join([str(x) for x in magic_sequence])}")


for toy, count in sorted(toys_made.items()):
	print(f"{toy}: {count}")
