def students_credits(*args):
	result = []
	student_data = {}
	
	for arg in args:
		course_name, max_credits, \
			max_points, test_points = [int(x) if x.isdigit() else x for x in arg.split('-')]
		
		credits_ = max_credits * (test_points / max_points)
		student_data[course_name] = credits_
		
	total_credits_earned = sum([num for num in student_data.values()])
	
	if total_credits_earned >= 240:
		result.append(f"Diyan gets a diploma with {total_credits_earned:.1f} credits.")
	else:
		result.append(f"Diyan needs {240 - total_credits_earned:.1f} credits more for a diploma.")

	for course, credit in sorted(student_data.items(), key=lambda x: -x[1]):
		result.append(f"{course} - {credit:.1f}")
		
	return '\n'.join(result)

