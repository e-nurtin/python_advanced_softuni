def valid_info(data, comm):
	if comm == "swap" and len(data) == 4:
		coords_1, coords_2 = data[:2], data[2:]

		for coord in (coords_1, coords_2):
			if not 0 <= coord[0] < rows and not 0 <= coord[1] < columns:
				break
		else:
			return True
	return False


rows, columns = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]


while True:
	command = input()
	if command == "END":
		break

	action, *info = [int(x) if x.isdigit() else x for x in command.split()]

	if valid_info(info, action):
		matrix[info[0]][info[1]], matrix[info[2]][info[3]] = matrix[info[2]][info[3]], matrix[info[0]][info[1]]

		for row in matrix:
			print(*row)
		continue

	print("Invalid input!")

	