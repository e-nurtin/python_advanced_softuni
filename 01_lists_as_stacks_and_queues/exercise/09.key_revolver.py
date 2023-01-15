from collections import deque

price_per_bullet = int(input())
gun_barrel_size = int(input())
bullets = deque([int(x) for x in input().split()])
locks = deque([int(x) for x in input().split()])
value_of_intelligence = int(input())

barrel_count = 0
bullet_count = len(bullets.copy())

while locks:
	if not bullets:
		print(f"Couldn't get through. Locks left: {len(locks)}")
		break
		
	current_bullet = bullets.pop()
	barrel_count += 1
	
	if current_bullet <= locks[0]:
		current_lock = locks.popleft()
		print("Bang!")
	else:
		print("Ping!")
		
	if barrel_count == gun_barrel_size and bullets:
		print("Reloading!")
		barrel_count = 0
else:
	money_earned = value_of_intelligence - (bullet_count - len(bullets)) * price_per_bullet
	print(f"{len(bullets)} bullets left. Earned ${money_earned}")
	