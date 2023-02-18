square_n = 6

matrix = [input().split() for row in range(square_n)]
total_points = 0
hit_buckets = []

for _ in range(3):
	throw = input().split(', ')
	r, c = int(throw[0][1:]), int(throw[1][:-1])
	
	if not (0 <= r < square_n and 0 <= c < square_n):
		continue
		
	if matrix[r][c] == "B":
		
		if (r, c) in hit_buckets:
			continue
		hit_buckets.append((r, c))
		points = 0
		
		for row in range(square_n):
			if matrix[row][c].isdigit():
				points += int(matrix[row][c])
		
		total_points += points

prize = ""
if 100 <= total_points <= 199:
	prize = "Football"
elif 200 <= total_points <= 299:
	prize = "Teddy Bear"
elif total_points >= 300:
	prize = "Lego Construction Set"

if prize:
	print(f"Good job! You scored {total_points} points, and you've won {prize}.")
else:
	print(f"Sorry! You need {100 - total_points} points more to win a prize.")
