# from collections import deque
#
# color_substrings = deque(input().split())
#
# found_colors = []
# found_secondary_colors = []
#
# primary_colors = ["red", "yellow", "blue"]
# #
# secondary_colors = {
# 	"orange": ["red", "yellow"],
# 	"purple": ["red", "blue"],
# 	"green": ["yellow", "blue"],
# }
#
# while len(color_substrings) > 1:
#
# 	first_substring = color_substrings.popleft()
# 	last_substring = color_substrings.pop()
#
# 	if first_substring + last_substring in primary_colors:
# 		found_colors.append(first_substring + last_substring)
#
# 	elif last_substring + first_substring in primary_colors:
# 		found_colors.append(last_substring + first_substring)
#
# 	elif first_substring + last_substring in secondary_colors:
# 		found_secondary_colors.append(first_substring + last_substring)
# 		found_colors.append(first_substring + last_substring)
#
# 	elif last_substring + first_substring in secondary_colors:
# 		found_secondary_colors.append(last_substring + first_substring)
# 		found_colors.append(last_substring + first_substring)
#
# 	else:
# 		index = len(color_substrings) // 2
# 		if len(first_substring) > 1:
# 			color_substrings.insert(index, first_substring[:-1])
# 		if len(last_substring) > 1:
# 			color_substrings.insert(index + 1, last_substring[:-1])
#
# last_substring = color_substrings.pop()
#
# if last_substring in primary_colors:
# 	found_colors.append(last_substring)
#
# elif last_substring in secondary_colors:
# 	found_secondary_colors.append(last_substring)
# 	found_colors.append(last_substring)
#
# if secondary_colors:
# 	keep_the_color = False
# 	for color in found_secondary_colors:
# 		for primary in secondary_colors[color]:
# 			if primary in found_colors:
# 				keep_the_color = True
# 				continue
# 			keep_the_color = False
# 		if not keep_the_color:
# 			found_colors.remove(color)
#
# print(found_colors)