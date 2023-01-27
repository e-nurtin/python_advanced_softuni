data = {}
for symbol in input():
	data[symbol] = data.get(symbol, 0) + 1

for symbol, count in sorted(data.items()):
	print(f"{symbol}: {count} time/s")

# text = input()
#
# data = {}
# for symbol in text:
# 	data[symbol] = text.count(symbol)
#
# for symbol, count in sorted(data.items()):
# 	print(f"{symbol}: {count} time/s")
#

