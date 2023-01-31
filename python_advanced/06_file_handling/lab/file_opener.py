import os

# with open('text.txt', 'r') as file:
# 	print()

a = os.path.dirname(os.path.abspath(__file__))

path = os.path.join(a, 'lel', 'male')
print(path)

try:
	file = open('text.txt', 'r')
	print('File found')
except FileNotFoundError:
	print("File not found")
	
file.close()
