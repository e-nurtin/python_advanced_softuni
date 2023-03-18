def reverse_text(string):
	start = len(string)
	end = 0
	while start != end:
		start -= 1
		yield string[start]


for char in reverse_text("step"):
	print(char, end='')
