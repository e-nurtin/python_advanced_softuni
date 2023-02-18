from collections import deque

seats = input().split(', ')

first_sequence = deque(input().split(', '))
last_sequence = deque(input().split(', '))

rotations = 0
matched_seats = []

while rotations < 10 and len(matched_seats) < 3:
	first_n = first_sequence.popleft()
	last_n = last_sequence.pop()
	
	rotations += 1
	letter = chr(int(first_n) + int(last_n))
	
	for combination in [first_n + letter, last_n + letter]:
		
		if combination in seats:
			matched_seats.append(seats.pop(seats.index(combination)))
			break
			
	else:
		first_sequence.append(first_n)
		last_sequence.insert(0, last_n)
		

print(f"Seat matches: {', '.join([x for x in matched_seats])}")
print(f"Rotations count: {rotations}")
