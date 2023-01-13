count_of_students = int(input())

student_info = {}

for _ in range(count_of_students):
	student, grade = input().split()
	
	if student not in student_info:
		student_info[student] = []
	
	student_info[student].append(float(grade))

for student, grades in student_info.items():
	average_grade = sum(grades) / len(grades)
	grades = ' '.join(map(lambda grade: f"{grade:.2f}", grades))
	print(f"{student} -> {grades} (avg: {average_grade:.2f})")
