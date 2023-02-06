from math import log
number_ = int(input())
base = input()

if base == "natural":
	print(f"{log(number_):.2f}")
else:
	print(f"{log(number_, int(base)):.2f}")

