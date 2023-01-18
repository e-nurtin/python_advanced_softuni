first_sequence = {int(x) for x in input().split()}
second_sequence = {int(x) for x in input().split()}

functions = {
	"Add First": lambda x: [first_sequence.add(el) for el in x],
	"Add Second": lambda x: [second_sequence.add(el) for el in x],
	"Remove First": lambda x: [first_sequence.remove(el) for el in x if el in first_sequence],
	"Remove Second": lambda x: [second_sequence.remove(el) for el in x if el in second_sequence],
	"Check Subset": lambda: print(True) if second_sequence.issubset(first_sequence) or first_sequence.issubset(second_sequence) else print(False),
}

for _ in range(int(input())):
	
	data = input().split()
	action = data[0] + ' ' + data[1]
	data = {int(x) for x in data[2:]}

	if data:
		functions[action](data)
	else:
		functions[action]()

# print(', '.join([str(x) for x in  sorted(first_sequence)]))
# print(', '.join([str(x) for x in sorted(second_sequence)]))

print(*sorted(first_sequence), sep=', ')
print(*sorted(second_sequence), sep=', ')
