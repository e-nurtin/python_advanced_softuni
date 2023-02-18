from collections import deque

players = deque(input().split(', '))
square_n = 6

matrix = [input().split() for row in range(square_n)]

while True:
	pos = input()
	r, c = int(pos[1]), int(pos[-2])
	
	current_player = players.popleft()
	
	if current_player.endswith('W'):
		players.append(current_player[:-1])
		continue
	
	if matrix[r][c] == 'E':
		print(f"{current_player} found the Exit and wins the game!")
		break
		
	elif matrix[r][c] == 'T':
		print(f"{current_player} is out of the game! The winner is {players.popleft()}.")
		break
		
	elif matrix[r][c] == 'W':
		print(f"{current_player} hits a wall and needs to rest.")
		current_player = current_player + "W"
		
	players.append(current_player)
	
