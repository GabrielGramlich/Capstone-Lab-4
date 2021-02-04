'''
Practice using
 assertTrue
 assertFalse
 assertIsNone
 assertIsNotNone
 assertIn
 assertNotIn
'''

from studentlists import ClassList, StudentError
from unittest import TestCase

class TestStudentLists(TestCase):

	def test_add_student_check_student_in_list(self):
		test_class = ClassList(2)
		test_class.add_student('Test Student')
		self.assertIn('Test Student', test_class.class_list)

		test_class.add_student('Another Test Student')
		self.assertIn('Test Student', test_class.class_list)
		self.assertIn('Another Test Student', test_class.class_list)


	def test_add_student_already_in_list(self):
		test_class = ClassList(2)
		test_class.add_student('Test Student')
		with self.assertRaises(StudentError):
			test_class.add_student('Test Student')


	def test_add_remove_student_ensure_removed(self):
		test_class = ClassList(2)
		test_class.add_student('Test Student')
		self.assertIn('Test Student', test_class.class_list)
		test_class.remove_student('Test Student')
		self.assertNotIn('Test Student', test_class.class_list)


	def test_remove_student_who_is_not_in_the_list_raises_student_error(self):
		test_class = ClassList(5)
		test_class.add_student('Punky Brewster')
		test_class.add_student('Doogie Howser')
		test_class.add_student('Webster Long')

		with self.assertRaises(StudentError):
			test_class.remove_student('Arnold Jackson')


	def test_remove_student_from_an_empty_list_raises_student_error(self):
		test_class = ClassList(5)

		with self.assertRaises(StudentError):
			test_class.remove_student('Clara James')


	def test_is_enrolled_when_student_present(self):
		test_class = ClassList(2)
		test_class.add_student('Snoop Dogg')
		test_class.add_student('Martha Stewart')
		self.assertTrue(test_class.is_enrolled('Snoop Dogg'))
		self.assertTrue(test_class.is_enrolled('Martha Stewart'))


	def test_is_enrolled_empty_class_list(self):
		test_class = ClassList(2)
		self.assertFalse(test_class.is_enrolled('Snoop Dogg'))


	def test_student_not_in_class_is_not_enrolled(self):
		test_class = ClassList(4)
		test_class.add_student('Alice')
		test_class.add_student('Bob')

		is_carl_enrolled = test_class.is_enrolled('Carl')

		self.assertFalse(is_carl_enrolled)


	def test_string_with_students_enrolled(self):
		test_class = ClassList(2)
		test_class.add_student('Taylor Swift')
		test_class.add_student('Kanye West')
		self.assertEqual('Taylor Swift, Kanye West', str(test_class))


	def test_string_empty_class(self):
		test_class = ClassList(2)
		self.assertEqual('', str(test_class))


	def test_index_of_student_student_present(self):
		test_class = ClassList(3)
		test_class.add_student('Harry')
		test_class.add_student('Hermione')
		test_class.add_student('Ron')

		self.assertEqual(1, test_class.index_of_student('Harry'))
		self.assertEqual(2, test_class.index_of_student('Hermione'))
		self.assertEqual(3, test_class.index_of_student('Ron'))

		# This assert passes, but it's redundant - the first assert statement will fail if
		# the method call returns None
		self.assertIsNotNone(test_class.index_of_student('Harry'))



	def test_index_of_student_in_empty_list_returns_none(self):
	## TODO write a test for index_of_student when the class_list list is empty.  
	# Assert index_of_student returns None for a student if the list is empty. 
	# use assertIsNone.
		test_class = ClassList(5)

		index_of_missing_student = test_class.index_of_student('Clement Attlee')

		self.assertIsNone(index_of_missing_student)


	## TODO write another test for index_of_student. In the case when the 
	# class_list is not empty but has some students.
	# assert that searching for a student name that is not in the list, returns None.


	def test_class_full_returns_true(self):
		test_class = ClassList(3)
		test_class.add_student('Harry')
		test_class.add_student('Hermione')
		test_class.add_student('Ron')

		result = test_class.is_class_full()
		self.assertTrue(result)


	## TODO write a test for your new is_class_full method for when is empty, 
	# and when it is not full. Use assertFalse.


