numbers = tuple(map(float, input().split()))

# numbers_count = {number: numbers.count(number) for number in numbers}
numbers_count = {}
for number in numbers:
	if number not in numbers_count:
		numbers_count[number] = 0
	numbers_count[number] += 1
	
for number, count in numbers_count.items():
	print(f"{number} - {count} times")
