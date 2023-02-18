from collections import deque

bowls_of_ramen = deque([int(x) for x in input().split(', ')])
customers = deque([int(x) for x in input().split(', ')])
current_bowl = 0
current_customer = 0

while bowls_of_ramen and customers:
	current_customer = customers.popleft()
	current_bowl = bowls_of_ramen.pop()
	
	if current_customer < current_bowl:
		current_bowl -= current_customer
		bowls_of_ramen.append(current_bowl)
		
	elif current_customer > current_bowl:
		current_customer -= current_bowl
		customers.appendleft(current_customer)
	

if not customers:
	print(f"Great job! You served all the customers.")
	if bowls_of_ramen:
		print(f"Bowls of ramen left: {', '.join([str(x) for x in bowls_of_ramen])}")
else:
	print("Out of ramen! You didn't manage to serve all customers.")
	if customers:
		print(f"Customers left: {', '.join([str(x) for x in customers])}")
		