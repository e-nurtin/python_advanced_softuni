equation = input()
list_of_parentheses_indexes = []
opening_i = -1
for index in range(len(equation)):
    current_symbol = equation[index]
    
    if current_symbol == "(":
        list_of_parentheses_indexes.append(index)
        
    elif current_symbol == ")":
        opening_i = int(list_of_parentheses_indexes.pop())
        print(equation[opening_i:index + 1])
