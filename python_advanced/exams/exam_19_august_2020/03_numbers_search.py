def numbers_searching(*numbers):
	range_of_numbers = set(range(min(numbers), max(numbers) + 1))
	
	missing_number = [number for number in range_of_numbers if number not in numbers]
	duplicates = set([number for number in numbers if numbers.count(number) > 1])
	missing_number.append(list(sorted(duplicates)))
	
	return missing_number
	
