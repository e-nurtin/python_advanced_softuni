from collections import deque

eggs = deque([int(x) for x in input().split(', ')])
papers = deque([int(x) for x in input().split(', ')])
boxes_filled = 0

while eggs and papers:
	current_egg = eggs.popleft()
	
	if current_egg == 13:
		papers[0], papers[-1] = papers[-1], papers[0]
		continue
		
	elif current_egg <= 0:
		continue
	
	current_paper = papers.pop()
	
	if current_paper + current_egg <= 50:
		boxes_filled += 1
	
if boxes_filled:
	print(f"Great! You filled {boxes_filled} boxes.")
else:
	print("Sorry! You couldn't fill any boxes!")
	
if eggs:
	print(f"Eggs left: {', '.join([str(egg) for egg in eggs])}")
	
if papers:
	print(f"Pieces of paper left: {', '.join([str(paper) for paper in papers])}")
	
