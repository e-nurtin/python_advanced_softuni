from itertools import permutations


def possible_permutations(items):
	perms = permutations(items)
	for permutation in perms:
		yield list(permutation)


for i in possible_permutations([1, 2, 3]):
	print(i)
