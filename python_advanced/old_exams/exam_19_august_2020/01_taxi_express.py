from collections import deque

customers = deque([int(x) for x in input().split(', ')])
taxis = deque([int(x) for x in input().split(', ')])

total_time = 0

while customers and taxis:
	current_taxi = taxis.pop()
	current_customer = customers.popleft() if current_taxi >= customers[0] else 0
	
	if current_customer == 0:
		continue
	
	total_time += current_customer
	
if customers:
	print(f"Not all customers were driven to their destinations")
	print(f"Customers left: {', '.join([str(x) for x in customers])}")

else:
	print("All customers were driven to their destinations")
	print(f"Total time: {total_time} minutes")