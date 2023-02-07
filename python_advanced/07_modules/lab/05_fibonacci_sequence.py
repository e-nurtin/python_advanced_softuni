from fibbonacci import print_fibonacci, locate_number_in_sequence

sequence = []
while True:
	command = input()
	
	if command == 'Stop':
		break
	elif "Create" in command:
		sequence = print_fibonacci(int(command.split()[2]))
		print(' '.join([str(x) for x in sequence]))
	elif "Locate" in command:
		number_ = int(command.split()[1])
		result = locate_number_in_sequence(sequence, number_)
		if result:
			print(f"The number - {number_} is at index {result}")
		else:
			print(f"The number {number_} is not in the sequence")