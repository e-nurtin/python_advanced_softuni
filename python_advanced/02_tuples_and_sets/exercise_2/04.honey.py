from collections import deque

working_bees = deque(list(map(int, input().split())))
nectars = deque(list(map(int, input().split())))
symbols = deque(input().split())

total_honey = 0

arithmetic = {
	'+': lambda bee, nectar: bee + nectar,
	'-': lambda bee, nectar: bee - nectar,
	'*': lambda bee, nectar: bee * nectar,
	'/': lambda bee, nectar: bee / nectar,
}

while working_bees and nectars:
	
	current_nectar = nectars.pop()
	if current_nectar < working_bees[0]:
		continue
		
	bee_with_nectar = working_bees.popleft()
	if current_nectar != 0:
		total_honey += abs(arithmetic[symbols.popleft()](bee_with_nectar, current_nectar))

print(f"Total honey made: {total_honey}")

if working_bees:
	print(f"Bees left: {', '.join([str(bee) for bee in working_bees])}")
if nectars:
	print(f"Nectar left: {', '.join([str(nectar) for nectar in nectars])}")
	