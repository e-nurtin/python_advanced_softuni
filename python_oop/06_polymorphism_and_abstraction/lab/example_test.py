# class Tax:
# 	def calculate_tax(self, annual_income):
# 		return annual_income * 0.2
#
#
# class Person(Tax):
# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age
#
#
# class Chef(Person):
# 	def __init__(self, name, age, annual_income):
# 		super().__init__(name, age)
# 		self.annual_income = annual_income
#
#
# class Attorney(Person):
# 	def __init__(self, name, age, annual_income):
# 		super().__init__(name, age)
# 		self.annual_income = annual_income
#
#
# class Employee(Person):
# 	def __init__(self, name, age, annual_income):
# 		super().__init__(name, age)
# 		self.annual_income = annual_income
#
#
# employees = [Employee('mark', 30, 21000), Chef("Max", 28, 30600), Attorney("Helen", 43, 35000)]
#
# for employee in employees:
# 	print(employee.calculate_tax(employee.annual_income))


key = list(map(int, input().split()))


def find_items(curr_line, start_s, end_s):
	start = curr_line.find(start_s)
	end = curr_line.find(end_s, start + 1)
	return curr_line[start + 1:end]


while True:
	command = input()
	if command == "find":
		break
	line = list(command)
	for i in range(len(line)):
		num = key[i % len(key)]
		line[i] = chr(ord(line[i]) - num)
	final_line = "".join(line)
	type_treasure = find_items(final_line, "&", '&')
	
	coordinates = find_items(final_line, '<', '>')
	start_coordinates, end_coordinates = final_line.find("<"), final_line.find(">")
	# coordinates = final_line[start_coordinates + 1:end_coordinates]
	print(f"Found {type_treasure} at {coordinates}")