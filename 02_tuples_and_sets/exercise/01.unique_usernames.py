# print('\n'.join(set([input() for x in range(int(input()))])))

count_of_names = int(input())
names = set()

for _ in range(count_of_names):
	names.add(input())

print('\n'.join(names))
