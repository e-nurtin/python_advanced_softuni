from itertools import permutations


def possible_permutations(items):
	perms = permutations(items)
	for i in perms:
		yield list(i)


for i in possible_permutations([1, 2, 3]):
	print(i)
