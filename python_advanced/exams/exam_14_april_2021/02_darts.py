def get_corresponding_numbers(row, col):
	return dart_board[row][0] + dart_board[row][board_n - 1] + dart_board[0][col] + dart_board[board_n - 1][col]


board_n = 7
winner, throws = "", 0
player_one, player_two = input().split(', ')

# player_data index 0 for player represents their numbers and index 1 for their count of throws
player_data = {
	player_one: [501, 0],
	player_two: [501, 0],
}
dart_board = [[int(x) if x.isdigit() else x for x in input().split()] for row in range(board_n)]


turn = player_one
# cycle continues until one of the players reaches 0 or less
while True:
	player_data[turn][1] += 1
	points = 0
	
	throw = input().split(', ')
	r, c = int(throw[0][1:]), int(throw[1][:-1])
	
	if 0 <= r < board_n and 0 <= c < board_n:
	
		element = dart_board[r][c]
		if element == 'D':
			points = (get_corresponding_numbers(r, c)) * 2
		
		elif element == 'T':
			points = (get_corresponding_numbers(r, c)) * 3
			
		elif element == 'B':
			player_data[turn][0] = 0
			
		else:
			points = element
		
		player_data[turn][0] -= points
		
		if player_data[turn][0] <= 0:
			winner, throws = turn, player_data[turn][1]
			break
	
	if turn == player_one:
		turn = player_two
	else:
		turn = player_one
		

# winner_data = [(key, value[1]) for key, value in player_data.items() if value[0] <= 0]
print(f"{winner} won the game with {throws} throws!")
