from collections import deque

color_substrings = deque(input().split())

found_colors = []

colors = {
	"all colors": ("red", "yellow", "blue", "orange", "purple", "green"),
	"required_colors": {
		"orange": ("red", "yellow"),
		"purple": ("red", "blue"),
		"green": ("yellow", "blue"),
	},
}

while color_substrings:
	last_substring = ""
	if len(color_substrings) > 1:
		last_substring = color_substrings.pop()
	first_substring = color_substrings.popleft()

	for color in (first_substring + last_substring, last_substring + first_substring):
		if color in colors['all colors']:
			found_colors.append(color)
			break
	else:
		for item in (first_substring[:-1], last_substring[:-1]):
			if item:
				color_substrings.insert(len(color_substrings) // 2, item)
				

for color, required in colors["required_colors"].items():
	if any(x not in found_colors and color in found_colors for x in required):
		found_colors.remove(color)

print(found_colors)
