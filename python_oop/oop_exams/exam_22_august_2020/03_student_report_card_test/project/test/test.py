from project.student_report_card import StudentReportCard
from unittest import TestCase, main


class StudentReportCardTest(TestCase):
	def setUp(self):
		self.student_rc = StudentReportCard('student', 2)
	
	def test_init(self):
		assert 'student' == self.student_rc.student_name
		assert 2 == self.student_rc.school_year
		assert isinstance(self.student_rc.grades_by_subject, dict)
		assert {} == self.student_rc.grades_by_subject
	
	def test_name_setter_empty_value_raises(self):
		with self.assertRaises(ValueError) as ex:
			self.student_rc.student_name = ""
		expected = "Student Name cannot be an empty string!"
		assert expected == str(ex.exception)
	
	def test_school_year_setter_high_value_raises(self):
		with self.assertRaises(ValueError) as ex:
			self.student_rc.school_year = 15
		expected = "School Year must be between 1 and 12!"
		assert expected == str(ex.exception)
	
	def test_school_year_setter_high_value_raises(self):
		with self.assertRaises(ValueError) as ex:
			self.student_rc.school_year = 15
		expected = "School Year must be between 1 and 12!"
		assert expected == str(ex.exception)
	
	def test_school_year_setter_low_value_raises(self):
		with self.assertRaises(ValueError) as ex:
			self.student_rc.school_year = 0
		expected = "School Year must be between 1 and 12!"
		assert expected == str(ex.exception)
	
	def test_add_grade_method_works(self):
		self.student_rc.add_grade('subject1', 5.5)
		assert {'subject1': [5.5]} == self.student_rc.grades_by_subject
		
		self.student_rc.add_grade('subject1', 4.5)
		self.student_rc.add_grade('subj2', 3)
		assert isinstance(self.student_rc.grades_by_subject['subject1'], list)
		assert {'subject1': [5.5, 4.5], 'subj2': [3]} == self.student_rc.grades_by_subject
	
	def test_average_grade_by_student_method_works(self):
		self.student_rc.add_grade('subject1', 5.5)
		self.student_rc.add_grade('subject1', 4.5)
		self.student_rc.add_grade('subject2', 2.5)
		self.student_rc.add_grade('subject2', 3.5)
		
		expected = "subject1: 5.00\nsubject2: 3.00"
		result = self.student_rc.average_grade_by_subject()
		
		assert expected == result
	
	def test_average_grade_for_all_subjects_works(self):
		self.student_rc.add_grade('subject1', 5.5)
		self.student_rc.add_grade('subject1', 4.5)
		self.student_rc.add_grade('subject2', 2.5)
		self.student_rc.add_grade('subject2', 3.5)
		expected = 'Average Grade: 4.00'
		result = self.student_rc.average_grade_for_all_subjects()
		assert expected == result
	
	def test__repr__method_returns_correct_message(self):
		self.student_rc.add_grade('subject1', 4.5)
		self.student_rc.add_grade('subject2', 2.5)
		expected = "Name: student\nYear: 2\n----------\nsubject1: 4.50\nsubject2: 2.50\n----------\nAverage Grade: 3.50"
		result = str(self.student_rc)
		assert expected == result
	
	def test_private_attr_exists(self):
		assert "student" == self.student_rc._StudentReportCard__student_name
		assert 2 == self.student_rc._StudentReportCard__school_year


if __name__ == '__main__':
	main()
