parentheses_sequence = list(input())

parentheses_indexes = []
opening_brackets = ['{', '[', '(']
closing_brackets = ['}', ']', ')']

balanced_parentheses = False
if len(parentheses_sequence) % 2 == 0:
    for index in range(len(parentheses_sequence)):

        if parentheses_sequence[index] in opening_brackets:
            parentheses_indexes.append(index)

        elif parentheses_sequence[index] in closing_brackets and len(parentheses_indexes) > 0:

            opening = opening_brackets.index(parentheses_sequence[parentheses_indexes.pop(-1)])
            closing = closing_brackets.index(parentheses_sequence[index])

            if opening == closing:
                balanced_parentheses = True
        else:
            balanced_parentheses = False
            break

if balanced_parentheses and len(parentheses_indexes) == 0:
    print('YES')
else:
    print('NO')
