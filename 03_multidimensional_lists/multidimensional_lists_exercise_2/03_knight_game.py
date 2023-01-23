def find_possible_knights():
	for k_r, k_c in knights.keys():
		current_knight_moves = []
		
		for i in range(-2, 3):
			for j in range(-2, 3):
				
				# Using pythagorean theorem to find out possible moves of a knight and checking correct index
				if i ** 2 + j ** 2 == 5 and (0 <= k_r + i < n and 0 <= k_c + j < n):
					
					if matrix[k_r + i][k_c + j] == 'K':
						current_knight_moves.append((k_r + i, k_c + j))
						
		knights[(k_r, k_c)] = current_knight_moves


n = int(input())

matrix, knights = [], {}
knights_removed = 0

for r in range(n):
	matrix.append(list(input()))
	for c in range(n):
		
		if matrix[r][c] == 'K':
			knights[(r, c)] = []

find_possible_knights()

while any([len(x) > 0 for x in knights.values()]):
	max_attack_knight = max([len(x) for x in knights.values()])
	
	for key, value in knights.items():
		
		if len(value) == max_attack_knight and max_attack_knight > 0:
			matrix[key[0]][key[1]] = '0'
			
			del knights[key]
			knights_removed += 1
			break
		
	find_possible_knights()

print(knights_removed)
