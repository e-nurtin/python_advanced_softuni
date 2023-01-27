from collections import deque
from functools import reduce

expression = input().split()
current_symbols = deque()

operators = {
	'*': lambda a, b: (int(a) * int(b)),
	'+': lambda a, b: (int(a) + int(b)),
	'/': lambda a, b: (int(a) / int(b)),
	'-': lambda a, b: (int(a) - int(b)),
}

index = 0
while index < len(expression):
	
	if expression[index] in operators:
		result = reduce(lambda x, y: operators[expression[index]](x, y), expression[:index])
		expression = expression[index:]
		expression[0] = result
		index = 0
		
	index += 1
	
print(int(expression.pop()))

#
#
# 2
#
#
# from collections import deque
#
# expression = input().split()
# current_symbols = deque()
#
# operators = {
# 	'*': lambda num: num * current_symbols.popleft(),
# 	'+': lambda num: num + current_symbols.popleft(),
# 	'/': lambda num: num // current_symbols.popleft(),
# 	'-': lambda num: num - current_symbols.popleft(),
# }
#
# for symbol in expression:
#
# 	if symbol in operators:
# 		number = current_symbols.popleft()
#
# 		while current_symbols:
# 			number = operators[symbol](number)
#
# 		current_symbols.append(number)
#
# 	else:
# 		current_symbols.append(int(symbol))
#
# print(current_symbols.popleft())
#
#

# 1
#
#
# def operator_seen(operator):
# 	current_sum = current_symbols.popleft()
#
# 	if operator == '*':
# 		while current_symbols:
# 			current_sum *= current_symbols.popleft()
#
# 	elif operator == '+':
# 		while current_symbols:
# 			current_sum += current_symbols.popleft()
#
# 	elif operator == '-':
# 		while current_symbols:
# 			current_sum -= current_symbols.popleft()
#
# 	elif operator == '/':
# 		while current_symbols:
# 			current_sum //= current_symbols.popleft()
#
# 	current_symbols.append(current_sum)
#
#
# expression = input().split()
#
#
# possible_operators = '*+-/'
# current_symbols = deque()
#
# for symbol in expression:
#
# 	if symbol in possible_operators:
# 		operator_seen(symbol)
#
# 	else:
# 		current_symbols.append(int(symbol))
#
# print(current_symbols.popleft())
