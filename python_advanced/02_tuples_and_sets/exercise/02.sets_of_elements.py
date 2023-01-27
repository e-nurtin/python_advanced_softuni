count_1, count_2 = [int(x) for x in input().split()]

set_1 = set(int(input()) for x in range(count_1))
set_2 = set(int(input()) for x in range(count_2))

unique_items = set_1.intersection(set_2)

print(*unique_items, sep='\n')
