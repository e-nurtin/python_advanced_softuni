from functools import reduce


def operate(operator, *args):
	""" This only works if the divisor is not zero."""
	result = reduce(lambda x, y: eval(f"{x}{operator}{y}"), args)
	return result


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
print(operate("/", 23, 4))
