def add(digits, sequence):
	if sequence == 'First':
		first_sequence.union(digits)
	elif sequence == 'Second':
		second_sequence.union(digits)
	

def remove(digits, sequence):
	if sequence == 'First':
		first_sequence.difference(digits)
	elif sequence == 'Second':
		second_sequence.difference(digits)


def check_subset():
	if first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence):
		return True
	return False


first_sequence = set(map(int, input().split()))
second_sequence = set(map(int, input().split()))


for _ in range(int(input())):
	
	command = input()
	
	action, info, *numbers = [x if x.isalpha() else int(x) for x in command.split()]
	numbers = set(numbers)
	
	if action == "Add":
		add(numbers, info)
	
	elif action == "Remove":
		remove(numbers, info)
		
	elif action == "Check":
		print(check_subset())
		

# print(', '.join([str(x) for x in sorted(first_sequence)]))
# print(', '.join([str(x) for x in sorted(second_sequence)]))

print(*sorted(first_sequence), sep=', ')
print(*sorted(second_sequence), sep=', ')