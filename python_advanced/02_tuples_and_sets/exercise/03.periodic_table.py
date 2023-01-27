count_of_inputs = int(input())

elements = []

for _ in range(count_of_inputs):
	elements.extend(input().split())
	
print('\n'.join(set(elements)))
