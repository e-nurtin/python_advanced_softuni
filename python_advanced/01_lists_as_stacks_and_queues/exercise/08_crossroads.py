from collections import deque

green_light_duration = int(input())
free_window = int(input())

car_count = 0
cars_waiting_to_pass = deque()

command = input()
while command != "END":
	
	if command == 'green':
		current_green = green_light_duration
		
		while current_green > 0:
			
			if cars_waiting_to_pass:
				current_car = cars_waiting_to_pass.popleft()
				
				if current_green + free_window < len(current_car):
					print("A crash happened!")
					print(f"{current_car} was hit at {current_car[current_green + free_window]}.")
					exit()
					
				current_green -= len(current_car)
				car_count += 1
				
			else:
				break
	else:
		cars_waiting_to_pass.append(command)
		
	command = input()

else:
	print(f"Everyone is safe.")
	print(f"{car_count} total cars passed the crossroads.")
	