count_of_inputs = int(input())

even_numbers = set()
odd_numbers = set()

for row in range(1, count_of_inputs + 1):
	current_name = input()
	
	current_sum = int(sum([int(ord(x)) for x in current_name]) / row)
	
	if current_sum % 2 != 0:
		odd_numbers.add(current_sum)
	else:
		even_numbers.add(current_sum)

sum_even = sum(even_numbers)
sum_odd = sum(odd_numbers)

if sum_even == sum_odd:
	print(*odd_numbers.union(even_numbers), sep=', ')
elif sum_odd > sum_even:
	print(*odd_numbers.difference(even_numbers), sep=', ')
else:
	print(*odd_numbers.symmetric_difference(even_numbers), sep=', ')
