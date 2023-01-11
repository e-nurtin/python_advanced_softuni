# list_of_numbers = [int(x) for x in input().split()]
# print(*list_of_numbers[-1::-1], sep=' ')
#
#
# list_of_numbers = input().split()
# print(' '.join(list_of_numbers[-1::-1]))
#

stack = [int(x) for x in input().split()]
while stack:
	current_number = stack.pop()
	print(current_number, end=' ')