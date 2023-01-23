total_presents = int(input())
n = int(input())

santa_pos, matrix = [], []
count_nice_kids, happy_nice_kids = 0, 0

directions = {
	'up': (-1, 0),
	'down': (1, 0),
	'left': (0, -1),
	'right': (0, 1),
}

for r in range(n):
	matrix.append(input().split())
	
	if "S" in matrix[r]:
		santa_pos = [r, matrix[r].index("S")]
		matrix[r][santa_pos[1]] = '-'
		
	if "V" in matrix[r]:
		count_nice_kids += matrix[r].count("V")


while total_presents > 0:
	command = input()
	
	if command == "Christmas morning":
		break

	r, c = santa_pos[0] + directions[command][0], santa_pos[1] + directions[command][1]

	matrix[santa_pos[0]][santa_pos[1]] = '-'
	santa_pos = [r, c]

	if matrix[r][c] == "V":
		happy_nice_kids += 1
		total_presents -= 1

	elif matrix[r][c] == "C":

		for row, col in directions.values():
			row, col = r + row, c + col

			if matrix[row][col] == 'V':
				total_presents -= 1
				happy_nice_kids += 1

			elif matrix[row][col] == 'X':
				total_presents -= 1

			matrix[row][col] = '-'

	matrix[r][c] = 'S'


if not total_presents and happy_nice_kids < count_nice_kids:
	print("Santa ran out of presents!")

[print(' '.join(row)) for row in matrix]

if count_nice_kids == happy_nice_kids:
	print(f"Good job, Santa! {happy_nice_kids} happy nice kid/s.")
else:
	print(f"No presents for {count_nice_kids - happy_nice_kids} nice kid/s.")

