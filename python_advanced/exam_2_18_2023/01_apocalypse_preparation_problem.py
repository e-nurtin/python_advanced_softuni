from collections import deque

textiles = deque([int(x) for x in input().split()])
medicaments = deque([int(x) for x in input().split()])

items = {
	30: 'Patch',
	40: 'Bandage',
	100: 'MedKit',
}

made_items = {}

while textiles and medicaments:
	current_textile = textiles.popleft()
	current_med = medicaments.pop()
	
	sum_of_items = current_textile + current_med
	
	if sum_of_items in items:
		made_items[items[sum_of_items]] = made_items.get(items[sum_of_items], 0) + 1
	
	elif sum_of_items > max(items):
		made_items[items[max(items)]] = made_items.get(items[max(items)], 0) + 1
		
		if medicaments:
			medicaments[-1] += sum_of_items - max(items)
		else:
			medicaments.append(sum_of_items - max(items))
	
	else:
		medicaments.append(current_med + 10)

if not textiles and not medicaments:
	print("Textiles and medicaments are both empty.")
elif not textiles:
	print("Textiles are empty.")
elif not medicaments:
	print("Medicaments are empty.")

for item, count in sorted(made_items.items(), key=lambda x: (-x[1], x[0])):
	print(f"{item} - {count}")

medicaments = list(medicaments)
if medicaments:
	print(f"Medicaments left: {', '.join([str(x) for x in medicaments[::-1]])}")
if textiles:
	print(f"Textiles left: {', '.join([str(x) for x in textiles])}")

