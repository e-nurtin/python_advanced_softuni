from collections import deque
from math import ceil


def check_for_draw(matrix):
	for row in range(board_size):
		for col in range(board_size):
			if matrix[row][col] == ' ':
				return False
	return True


def check_for_possible_win(matrix, player_symbol):
	check_horizontal = any([all(player_symbol == symbol for symbol in row) for row in matrix])
	check_vertical = any([all(matrix[r][c] == player_symbol for r in range(board_size)) for c in range(board_size)])
	
	check_right_diagonal = all([matrix[i][board_size - i - 1] == player_symbol for i in range(board_size)])
	check_left_diagonal = all([matrix[i][i] == player_symbol for i in range(board_size)])
	
	if any([check_horizontal, check_vertical, check_right_diagonal, check_left_diagonal]):
		return True
	return False

	
def mark_player_choice_on_board(player_name, player_symbol, player_choice, matrix):
	while True:
		row = ceil(player_choice / board_size) - 1
		col = (player_choice - 1) % board_size
		
		if matrix[row][col] == ' ':
			matrix[row][col] = player_symbol
			
			[print(f"|  " + "  |  ".join(row), end='  |\n') for row in matrix]
			return matrix
		
		else:
			print('Chosen number is already taken!')
			player_choice = get_player_input(player_name)


def get_player_input(player_name):
	while True:
		player_input = input(f"{player_name}, please choose a number to put on the board: ")
		if player_input.isdigit():
			if 1 <= int(player_input) < 10:
				return int(player_input)
		print("Invalid input! Please choose a number between 1 and 9.")


def get_player_info():
	player_one_name = input("Player one please enter your name: ")
	player_two_name = input("Player two please enter your name: ")
	
	while True:
		player_one_symbol = input(f"{player_one_name} would you like to play with 'X' or 'O'?").upper()
		if player_one_symbol not in 'XO':
			print("Please enter 'X' or 'O'")
			continue
		break
	
	player_two_symbol = 'O' if player_one_symbol == 'X' else 'X'
	
	players.append([player_one_name, player_one_symbol])
	players.append([player_two_name, player_two_symbol])


def start_game():
	get_player_info()
	
	print('This is the numeration of the board')
	[print(f"|  " + "  |  ".join(row), end='  |\n') for row in board]
	matrix = [[' ' for _ in range(board_size)] for _ in range(board_size)]
	
	while True:
		player_in_turn = players.popleft()
		
		player_input = get_player_input(player_in_turn[0])
		matrix = mark_player_choice_on_board(player_in_turn[0], player_in_turn[1], int(player_input), matrix)
		
		if check_for_possible_win(matrix, player_in_turn[1]):
			print(f"Winner is {player_in_turn[0]}!")
			break
			
		if check_for_draw(matrix):
			print("Draw!")
			break
			
		players.append(player_in_turn)
	

players = deque([])
board = [[str(i), str(i + 1), str(i + 2)] for i in range(1, 10, 3)]
board_size = len(board)

start_game()
