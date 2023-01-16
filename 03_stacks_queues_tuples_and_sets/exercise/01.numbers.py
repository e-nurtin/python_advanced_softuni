def add(digits, sequence):
	if sequence == 'First':
		[first_sequence.add(num) for num in digits if num not in first_sequence]
	elif sequence == 'Second':
		[second_sequence.add(num) for num in digits if num not in second_sequence]
	

def remove(digits, sequence):
	if sequence == 'First':
		[first_sequence.remove(num) for num in digits if num in first_sequence]
	elif sequence == 'Second':
		[second_sequence.remove(num) for num in digits if num in second_sequence]


def check_subset():
	if first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence):
		return True
	return False


first_sequence = set(map(int, input().split()))
second_sequence = set(map(int, input().split()))


for _ in range(int(input())):
	
	command = input()
	
	action, info, *numbers = [x if x.isalpha() else int(x) for x in command.split()]
	
	if action == "Add":
		add(numbers, info)
	
	elif action == "Remove":
		remove(numbers, info)
		
	elif action == "Check":
		print(check_subset())
		

print(', '.join([str(x) for x in sorted(first_sequence)]))
print(', '.join([str(x) for x in sorted(second_sequence)]))

