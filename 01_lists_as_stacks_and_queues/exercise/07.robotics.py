from collections import deque
from datetime import datetime, timedelta

robots = {r.split('-')[0]: [int(r.split('-')[1]), 0] for r in input().split(';')}
copied_robots = deque(robots.copy())

time = datetime.strptime(input(), '%H:%M:%S')

products = deque()

product = input()
while product != "End":
	products.append(product)
	product = input()


while products:
	time += timedelta(0, 1)
	current_product = products.popleft()

	robots = {r: [v[0], v[1] - 1] if v[1] != 0 else v for r, v in robots.items()}
	free_robots = [r for r, v in robots.items() if v[1] == 0]
	
	# free_robots = []
	# for robot, value in robots.items():
	# 	if value[1] != 0:
	# 		robots[robot][1] -= 1
	#
	# for robot, value in robots.items():
	# 	if value[1] == 0:
	# 		free_robots.append(robot)

	if not free_robots:
		products.append(current_product)
		continue

	robots[free_robots[0]][1] = robots[free_robots[0]][0]
	print(f"{free_robots[0]} - {current_product} [{time.strftime('%H:%M:%S')}]")


	
