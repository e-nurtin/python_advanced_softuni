from collections import deque

chocolates = deque(list(map(int, input().split(', '))))
cups_of_milk = deque(list(map(int, input().split(', '))))

shake_counter = 0

while shake_counter < 5:
	if len(chocolates) > 0 and len(cups_of_milk) > 0:
		
		current_milk = cups_of_milk.popleft()
		
		if current_milk == chocolates[-1]:
			chocolates.pop()
			shake_counter += 1
			
		elif chocolates[-1] <= 0:
			chocolates.pop()
			cups_of_milk.appendleft(current_milk)
			
		elif current_milk <= 0:
			continue
			
		else:
			chocolates[-1] -= 5
			cups_of_milk.append(current_milk)
	else:
		print("Not enough milkshakes.")
		break
else:
	print("Great! You made all the chocolate milkshakes needed!")


print(f"Chocolate: {', '.join([str(x) for x in chocolates]) or 'empty'}")
print(f"Milk: {', '.join([str(x) for x in cups_of_milk]) or 'empty'}")
