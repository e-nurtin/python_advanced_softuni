equation = input()
list_of_parentheses_indexes = []
opening_i = -1
for index in range(len(equation)):
    if equation[index] == "(":
        list_of_parentheses_indexes.append(index)
    elif equation[index] == ")":
        opening_i = int(list_of_parentheses_indexes.pop(-1))
        print(equation[opening_i:index + 1])
