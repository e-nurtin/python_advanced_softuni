matrix = [[f"{chr(col)}{row}" for col in range(97, 97 + 8)] for row in range(8, 0, -1)]
pos = {
	"White": [],
	"Black": []
}
directions = {
	'White': [(-1, 1), (-1, -1), (-1, 0)],
	'Black': [(1, -1), (1, 1), (1, 0)]
}
opponent = {
	"White": "Black",
	"Black": "White",
}
for i in range(8):
	line = input().split()
	if "w" in line:
		pos['White'] = [i, line.index('w')]
	if "b" in line:
		pos['Black'] = [i, line.index('b')]

winner = ''
turn = 'White'
promoted = False
while True:
	r, c = pos[turn][0], pos[turn][1]
	opponent_pos = (pos[opponent[turn]][0], pos[opponent[turn]][1])
	
	for j, k in directions[turn][:2]:
		
		if (r + j, c + k) == opponent_pos:
			winner = turn
			pos[turn] = [r + j, c + k]
			break
	else:
		pos[turn] = [r + directions[turn][2][0], c + directions[turn][2][1]]
	
	if turn == 'White':
		if pos[turn][0] == 0:
			promoted = True
			winner = turn
		turn = 'Black'
		
	elif turn == 'Black':
		if pos[turn][0] == 7:
			promoted = True
			winner = turn
		turn = 'White'
		
	if promoted:
		print(f"Game over! {winner} pawn is promoted to a queen at {matrix[pos[winner][0]][pos[winner][1]]}.")
		break
		
	if winner:
		print(f"Game over! {winner} win, capture on {matrix[pos[winner][0]][pos[winner][1]]}.")
		break
