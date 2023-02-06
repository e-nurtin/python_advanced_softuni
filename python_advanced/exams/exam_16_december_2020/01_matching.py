from collections import deque

males = deque([int(x) for x in input().split()])
females = deque([int(x) for x in input().split()])
matches = 0

while males and females:
	male = males.pop() if females[0] > 0 or males[-1] <= 0 else 0
	female = females.popleft() if male > 0 or females[0] <= 0 else 0
	
	if male <= 0:
		continue
		
	if male % 25 == 0:
		if males:
			males.pop()
		females.appendleft(female)
		continue
		
	elif female % 25 == 0:
		if females:
			females.popleft()
		males.append(male)
		continue
	
	if male == female:
		matches += 1
	elif male > 2:
		males.append(male - 2)
		
print(f"Matches: {matches}")

if not males:
	males = ['none']
if not females:
	females = ['none']
	
print(f"Males left: {', '.join(str(male)for male in list(males)[::-1])}")
print(f"Females left: {', '.join(str(male)for male in list(females))}")
