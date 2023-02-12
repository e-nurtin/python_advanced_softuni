from sys import maxsize

jobs_to_be_done = [int(x) for x in input().split(', ')]
target_task = int(input())

time_spent = 0

for i in range(len(jobs_to_be_done)):
	
	current_task = jobs_to_be_done.index(min(jobs_to_be_done))
	time_spent += jobs_to_be_done[current_task]
	jobs_to_be_done[current_task] = maxsize
	
	if current_task == target_task:
		print(time_spent)
		break
		
