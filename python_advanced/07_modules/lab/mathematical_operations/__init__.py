def basic_expression_calculator(n1, operator, n2):
	"""
	:param operator: operator
	:param n1: number one
	:param n2: number two
	:return: result of operation
	"""
	possible_operators = {
		'+': lambda x, y: x + y,
		'-': lambda x, y: x - y,
		'*': lambda x, y: x * y,
		'/': lambda x, y: x / y,
		'^': lambda x, y: x ** y,
	}
	n1 = float(n1)
	n2 = int(n2)
	return f"{possible_operators[operator](n1, n2):.2f}"
