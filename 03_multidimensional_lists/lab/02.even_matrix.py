# using comprehension
#
print([[int(x) for x in input().split(', ') if int(x) % 2 == 0] for row in range(int(input()))])

#
# without comprehension
#
# rows = int(input())
# matrix = []
#
# for row in range(rows):
# 	matrix.append([])
# 	digits = [int(x) for x in input().split(', ')]
#
# 	for digit in digits:
# 		if digit % 2 == 0:
# 			matrix[row].append(digit)
# print(matrix)


