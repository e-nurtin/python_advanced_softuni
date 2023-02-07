from mathematical_operations import basic_expression_calculator

expression = input("Please enter the expression: ").split()
result = basic_expression_calculator(*expression)

print(f"Result is {result}")
