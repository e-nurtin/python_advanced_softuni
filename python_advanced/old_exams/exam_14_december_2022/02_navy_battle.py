square_n = int(input())

battlefield, ship_pos = [], []
mines_step_on, cruiser_kills = 0, 0

directions = {
	'up': (-1, 0),
	'down': (1, 0),
	'left': (0, -1),
	'right': (0, 1),
}


for row in range(square_n):
	battlefield.append(list(input()))
	if 'S' in battlefield[row]:
		ship_pos = [row, battlefield[row].index('S')]
		battlefield[row][ship_pos[1]] = '-'
	

while True:
	command = input()
	
	battlefield[ship_pos[0]][ship_pos[1]] = '-'
	
	r, c = ship_pos[0] + directions[command][0], ship_pos[1] + directions[command][1]
	element = battlefield[r][c]

	ship_pos = [r, c]
	
	if element == '*':
		mines_step_on += 1
		battlefield[r][c] = '-'
		
		if mines_step_on == 3:
			print(f"Mission failed, U-9 disappeared! Last known coordinates [{r}, {c}]!")
			break
	
	elif element == 'C':
		cruiser_kills += 1
		
		if cruiser_kills == 3:
			print(f"Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
			break


battlefield[r][c] = 'S'
[print(''.join(row)) for row in battlefield]
