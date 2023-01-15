count_of_intersections = int(input())


longest_intersection = []

for _ in range(count_of_intersections):
	first_range, second_range = [[int(i) for i in x.split(',')] for x in input().split('-')]
	first_set = set()
	second_set = set()
	
	for number in range(first_range[0], first_range[1] + 1):
		first_set.add(number)
		
	for number in range(second_range[0], second_range[1] + 1):
		second_set.add(number)
	
	current_section = first_set.intersection(second_set)

	if len(current_section) > len(longest_intersection):
		longest_intersection = current_section

numbers = ', '.join([str(x) for x in longest_intersection])
print(f"Longest intersection is [{numbers}] with length {len(longest_intersection)}")
