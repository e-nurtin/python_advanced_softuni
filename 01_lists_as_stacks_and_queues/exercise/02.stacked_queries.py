from collections import deque

stack = deque()
queries = [[int(x) for x in input().split()] for _ in range(int(input()))]

query_type = {
    1: lambda x: stack.append(x[1]),
    2: lambda x: stack.pop() if stack else None,
    3: lambda x: print(max(stack)) if stack else None,
    4: lambda x: print(min(stack)) if stack else None,
}

for query in queries:
    query_type[query[0]](query)

stack.reverse()
print(*stack, sep=', ')


# def push(numbers):
#     stack.append(numbers[1])
#     return stack
#
#
# def delete_n(*args):
#     if stack:
#         stack.pop()
#     return stack
#
#
# def print_max(*args):
#     if stack:
#         print(max(stack))
#     return stack
#
#
# def print_min(*args):
#     if stack:
#         print(min(stack))
#     return stack
#
#
# stack = []
# number_of_queries = int(input())
#
# query_data = {1: push, 2: delete_n, 3: print_max, 4: print_min}
#
# for n in range(number_of_queries):
#     current_query = [int(x) for x in input().split()]
#
#     stack = query_data[current_query[0]](current_query)
#
# print(*stack[-1::-1], sep=', ')