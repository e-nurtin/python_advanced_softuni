from unittest import TestCase, main
from project.student import Student


class StudentTests(TestCase):
	
	def test_student_init_when_no_courses(self):
		student = Student('TestName')
		
		self.assertEqual({}, student.courses)
	
	def test_student_init_when_courses_given(self):
		student = Student('TestName', {'Course1': [], 'course2': []})
		
		self.assertEqual({'Course1': [], 'course2': []}, student.courses)
	
	def test_if_given_courses_is_dict(self):
		student = Student('TestName')
		
		self.assertEqual(dict, type(student.courses))
	
	def test_student_init_name(self):
		student = Student('TestName')
		
		self.assertEqual('TestName', student.name)
	
	def test_enroll_method_course_name_already_exists(self):
		student = Student('TestName', {'Course1': [], 'course2': []})
		
		result = student.enroll('Course1', ['note1', 'note2'])
		expected = "Course already added. Notes have been updated."
		
		self.assertEqual(expected, result)
	
	def test_enroll_method_course_name_already_exists_notes_updated(self):
		student = Student('TestName', {'Course1': [], 'course2': []})
		
		student.enroll('Course1', ['note1', 'note2'])
		
		self.assertEqual(['note1', 'note2'], student.courses['Course1'])
	
	def test_enroll_method_if_course_notes_returns_with_Y(self):
		student = Student('TestName', {'Course1': [], 'course2': []})
		
		result = student.enroll('Course3', ['note1', 'note2'], 'Y')
		expected = "Course and course notes have been added."
		
		self.assertEqual(expected, result)
	
	def test_enroll_method_if_course_notes_returns_with_empty_str(self):
		student = Student('TestName', {'Course1': [], 'course2': []})
		
		result = student.enroll('Course3', ['note1', 'note2'], '')
		expected = "Course and course notes have been added."
		
		self.assertEqual(expected, result)
	
	def test_enroll_method_if_adds_course(self):
		student = Student('TestName', {'Course1': [], 'course2': []})
		
		student.enroll('Course3', ['note1', 'note2'], 'Y')
		self.assertIn('Course3', student.courses)
	
	def test_enroll_method_if_adds_notes(self):
		student = Student('TestName', {'Course1': [], 'course2': []})
		
		student.enroll('Course3', ['note1', 'note2'], 'Y')
		self.assertEqual(['note1', 'note2'], student.courses['Course3'])
	
	def test_enroll_method_if_course_notes_returns_with_wrong_notes(self):
		student = Student('TestName', {'Course1': [], 'course2': []})
		
		result = student.enroll('Course3', ['note1', 'note2'], 'asd')
		expected = "Course has been added."
		
		self.assertEqual(expected, result)
	
	def test_enroll_method_if_course_notes__with_wrong_notes_adds_course(self):
		student = Student('TestName', {'Course1': [], 'course2': []})
		
		student.enroll('Course3', ['note1', 'note2'], 'asd')
		
		self.assertIn('Course3', student.courses)
	
	def test_enroll_method_if_course_notes__with_wrong_notes_adds_course_list(self):
		student = Student('TestName', {'Course1': [], 'course2': []})
		
		student.enroll('Course3', ['note1', 'note2'], 'asd')
		
		self.assertEqual([], student.courses['Course3'])
	
	def test_add_notes_method_with_wrong_course_name_raises(self):
		student = Student('TestName', {'Course1': [], 'course2': []})
		
		with self.assertRaises(Exception) as exc:
			student.add_notes('cocon', 'note')
		
		expected = "Cannot add notes. Course not found."
		self.assertEqual(expected, str(exc.exception))
	
	def test_add_notes_method_adds_note(self):
		student = Student('TestName', {'Course1': [], 'course2': []})
		
		student.add_notes('course2', 'note')
		
		self.assertIn('note', student.courses['course2'])
	
	def test_add_notes_method_adds_note_returns(self):
		student = Student('TestName', {'Course1': [], 'course2': []})
		
		result = student.add_notes('course2', 'note')
		expected = "Notes have been updated"
		
		self.assertEqual(expected, result)
	
	def test_leave_course_method_wrong_name_raises(self):
		student = Student('TestName', {'Course1': [], 'course2': []})
		
		with self.assertRaises(Exception) as exc:
			student.leave_course('cocon')
		
		expected = "Cannot remove course. Course not found."
		self.assertEqual(expected, str(exc.exception))
	
	def test_leave_course_method_removes(self):
		student = Student('TestName', {'Course1': [], 'course2': []})
		
		student.leave_course('course2')
		
		self.assertNotIn('course2', student.courses)
	
	def test_leave_course_method_returns(self):
		student = Student('TestName', {'Course1': [], 'course2': []})
		
		result = student.leave_course('course2')
		expected = "Course has been removed"
		
		self.assertEqual(expected, result)


if __name__ == '__main__':
	main()
