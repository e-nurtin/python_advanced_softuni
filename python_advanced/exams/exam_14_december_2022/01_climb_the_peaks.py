from collections import deque

food_supplies = deque([int(x) for x in input().split(',')])
stamina = deque([int(x) for x in input().split(',')])
conquered_peaks = []

peaks = deque([
	('Vihren', 80),
	('Kutelo', 90),
	('Banski Suhodol', 100),
	('Polezhan', 60),
	('Kamenitza', 70),
])


while food_supplies and stamina and peaks:
	
	daily_food = food_supplies.pop()
	daily_stamina = stamina.popleft()
	
	peak, difficulty_level = peaks.popleft()
	
	if daily_stamina + daily_food >= difficulty_level:
		conquered_peaks.append(peak)
		continue
		
	else:
		peaks.insert(0, (peak, difficulty_level))

if len(conquered_peaks) == 5:
	print(f"Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
	print(f"Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered_peaks:
	peaks = '\n'.join(conquered_peaks)
	print(f"Conquered peaks: \n{peaks}")