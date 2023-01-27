def rectangle(length, width):
	if not (isinstance(length, int) and isinstance(width, int)):
		return f"Enter valid values!"
	
	def area(x, y):
		return x * y
	
	def perimeter(x, y):
		return 2 * (x + y)
	
	return f"Rectangle area: {area(length, width)}\nRectangle perimeter: {perimeter(length, width)}"


print(rectangle(2, 10))
print(rectangle('2', 10))
