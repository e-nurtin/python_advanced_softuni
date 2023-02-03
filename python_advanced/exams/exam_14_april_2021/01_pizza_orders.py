from collections import deque

pizza_orders = deque([int(x) for x in input().split(', ')])
employee_pizza_making_capacity = deque([int(x) for x in input().split(', ')])

total_pizzas_made = 0

while pizza_orders and employee_pizza_making_capacity:
	current_order = pizza_orders.popleft()
	
	if 0 >= current_order or current_order > 10:
		continue
		
	current_employee = employee_pizza_making_capacity.pop()
	
	if current_order > current_employee:
		
		current_order -= current_employee
		pizza_orders.appendleft(current_order)
		total_pizzas_made += current_employee
		continue
	
	total_pizzas_made += current_order

if pizza_orders:
	print("Not all orders are completed.")
else:
	print("All orders are successfully completed!")


if employee_pizza_making_capacity:
	print(f"Total pizzas made: {total_pizzas_made}")
	print(f"Employees: {', '.join([str(x) for x in employee_pizza_making_capacity])}")
if pizza_orders:
	print(f"Orders left: {', '.join([str(x) for x in pizza_orders])}")