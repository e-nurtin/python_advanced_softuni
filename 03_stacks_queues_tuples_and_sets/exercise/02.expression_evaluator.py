from collections import deque

expression = input().split()
current_symbols = deque()

operators = {
	'*': lambda num: num * current_symbols.popleft(),
	'+': lambda num: num + current_symbols.popleft(),
	'/': lambda num: num // current_symbols.popleft(),
	'-': lambda num: num - current_symbols.popleft(),
}

for symbol in expression:
	
	if symbol in operators:
		number = current_symbols.popleft()
		
		while current_symbols:
			number = operators[symbol](number)
			
		current_symbols.append(number)
		
	else:
		current_symbols.append(int(symbol))

print(current_symbols.popleft())

#
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
