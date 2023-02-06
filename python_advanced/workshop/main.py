import os
from collections import deque

"""
This game is console game based on the connect 4 game.
We start filling the matrix with the player numbers from bottom to top
and whoever first connects 4 of their number consecutively wins.
"""


# Draws a blank game board in the form of 2D array
def new_game():
	return [[0 for _ in range(COLUMN_SIZE)] for _ in range(ROW_SIZE)]


# TODO Save score to a file
# def save_data(winner, loser, filename='game_data.txt'):
# 	result = []
# 	if not os.path.exists(filename):
# 		with open(filename, 'w') as file:
# 			text = file.writelines(f"{winner} score: 0\n{loser} score: 0")
# 	with open(filename, 'r+') as file:
# 		text = file.readlines()
# 		for line in text:
# 			current_elements = line.split()
# 			if winner in line:
# 				print(current_elements[-1])
# 				line = f"{line[:-2]}{int(line[-2]) + 1}"
# 			print(line)
# 			result.append(line)
# 	with open(filename, 'w') as file:
# 		file.write('\n'.join(result))

# Gets current player's input and validates it
def get_player_input(player):
	while True:
		player_input = input(f"{player}, please choose a column\n")
		
		if player_input.isdigit():
			if 0 <= int(player_input) - 1 < COLUMN_SIZE:
				return int(player_input) - 1
		
		print(f"Invalid input! Please select a number between {1} and {COLUMN_SIZE}.")


# Marks the player's choice on the board in the chosen column if it is not full.
def mark_player_choice_on_board(column, player):
	row = ROW_SIZE
	for row in range(ROW_SIZE - 1, -1, -1):
		
		if board[row][column] == 0:
			board[row][column] = int(player[-1])
			[print(x) for x in board]
			print()
			break
	
	else:
		print("Column is full! Please choose another column.")
		column = get_player_input(player)
		mark_player_choice_on_board(column, player)
	return row, column


# Check if the row is on the border of the matrix or not and returns corresponding answer.
def check_board_borders(row, col, player):
	if any([0 > col, col >= COLUMN_SIZE, 0 > row, row >= ROW_SIZE]):
		return False
	return True


# Checks if the player in turn has won the game
def check_possible_winner(player, row, col, winner_count=4):
	vertical = check_vertical(col, player)
	horizontal = check_horizontal(row, player)
	diagonals = check_diagonals(row, col, player)

	if any([vertical, horizontal, diagonals]):
		return True


# Get all the elements in the current row and check if there's a winner
def check_horizontal(row, player, needed_consecutive=4):
	current_row = ''.join([str(x) for x in board[row]])
	if player * needed_consecutive in current_row:
		return True
	return False


# Get all the elements of the current column and check if there's a winner'
def check_vertical(col, player, needed_consecutive=4):
	current_col = ''.join([str(board[row][col]) for row in range(ROW_SIZE)])
	if player * needed_consecutive in current_col:
		return True
	return False


# Get all 4 of the elements in the diagonals and check if there's a winner'
def check_diagonals(row, col, player, needed_consecutive=4):
	right_up = ''.join(
		[str(board[row - i][col + i]) for i in range(COLUMN_SIZE) if check_board_borders(row - i, col + i, player)])
	left_down = ''.join(
		[str(board[row + i][col - i]) for i in range(1, COLUMN_SIZE) if check_board_borders(row + i, col - i, player)])
	
	left_up = ''.join(
		[str(board[row - i][col - i]) for i in range(COLUMN_SIZE) if check_board_borders(row - i, col - i, player)])
	right_down = ''.join(
		[str(board[row + i][col + i]) for i in range(1, COLUMN_SIZE) if check_board_borders(row + i, col + i, player)])
	
	if player * needed_consecutive in left_down + right_up or player * needed_consecutive in left_up + right_down:
		return True
	return False


ROW_SIZE = 7
COLUMN_SIZE = 6

game_count = 1
another_game = True
players = deque(["Player 1", "Player 2"])

board = new_game()

# Main Loop can continue playing after a game is over.
while another_game:
	
	player_in_turn = players.popleft()
	
	chosen_column = get_player_input(player_in_turn)
	r, c = mark_player_choice_on_board(chosen_column, player_in_turn)
	
	if check_possible_winner(player_in_turn[-1], r, c):
		print(f"Winner is {player_in_turn}")
		# save_data(player_in_turn, players[0])
		game = input(f"Do you want to play again? Press enter to play again\n")
		
		if game == "":
			board = new_game()
			game_count += 1
		else:
			another_game = False
	
	players.append(player_in_turn)
