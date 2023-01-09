def push(numbers):
    stack.append(numbers[1])
    return stack


def delete_n(*args):
    if stack:
        del stack[-1]
    return stack


def print_max(*args):
    if stack:
        print(max(stack))
    return stack


def print_min(*args):
    if stack:
        print(min(stack))
    return stack


stack = []
number_of_queries = int(input())
query_data = {1: push, 2: delete_n, 3: print_max, 4: print_min}
for n in range(number_of_queries):
    current_query = [int(x) for x in input().split()]
    stack = query_data[current_query[0]](current_query)

print(*stack[-1::-1], sep=', ')