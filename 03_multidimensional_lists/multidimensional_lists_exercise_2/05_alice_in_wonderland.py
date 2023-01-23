square_n = int(input())

matrix, alice_pos = [], []
tea_bags = 0

directions = {
	'up': (-1, 0),
	'down': (1, 0),
	'left': (0, -1),
	'right': (0, 1),
}

for row in range(square_n):
	matrix.append(input().split())
	for col in range(square_n):
		if matrix[row][col] == "A":
			alice_pos = [row, col]
			matrix[row][col] = '*'

while tea_bags < 10:
	command = input()

	r, c = alice_pos[0] + directions[command][0], alice_pos[1] + directions[command][1]
	
	if not (0 <= r < square_n and 0 <= c < square_n):
		break

	element = matrix[r][c]
	alice_pos = [r, c]
	matrix[r][c] = '*'

	if element.isdigit():
		tea_bags += int(element)

	elif element == "R":
		break

if tea_bags >= 10:
	print("She did it! She went to the party.")
else:
	print("Alice didn't make it to the tea party.")

[print(' '.join([str(x) for x in row])) for row in matrix]
