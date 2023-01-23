matrix = [[int(n) for n in input().split()] for row in range(int(input()))]

operations = {
	"Add": lambda x, y: x + y,
	"Subtract": lambda x, y: x - y,
}

command = input()
while command != "END":
	
	action, r, c, value = [i if i.isalpha() else int(i) for i in command.split()]
	
	if 0 <= r < len(matrix) and 0 <= c < len(matrix):
		matrix[r][c] = operations[action](matrix[r][c], value)
		
	else:
		print("Invalid coordinates")
	
	command = input()

[print(*row) for row in matrix]

