input_string = input()
list_of_string = list(input_string)
reversed_list = reversed(list_of_string)

# for i in reversed(list_of_string):
#     print(i, end='')
# reversed_list = list_of_string[-1::-1]
result = ''.join(reversed_list)
print(result)
