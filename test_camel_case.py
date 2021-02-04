import camel_case
from unittest import TestCase

class TestCamelCase(TestCase):

	def test_first_character_cannot_be_number(self):
		bad_string = '4this is a sentence'

		result = camel_case.check_first_character(bad_string)

		self.assertTrue(result)


	def test_first_character_can_be_string(self):
		bad_string = 'this is a sentence'

		result = camel_case.check_first_character(bad_string)

		self.assertFalse(result)


	def test_string_cannot_contain_special_characters(self):
		bad_string1 = 'this sen#tence is invalid'
		bad_string2 = 'this sentence is/ invalid'
		bad_string3 = 'this, sentence is invalid'
		bad_string4 = 'this sentence is inv\'alid'
		bad_string5 = 'this sentence \\is invalid'
		bad_string6 = 'this.sentence is invalid'

		result1 = camel_case.check_special_characters(bad_string1, False)
		result2 = camel_case.check_special_characters(bad_string2, False)
		result3 = camel_case.check_special_characters(bad_string3, False)
		result4 = camel_case.check_special_characters(bad_string4, False)
		result5 = camel_case.check_special_characters(bad_string5, False)
		result6 = camel_case.check_special_characters(bad_string6, False)

		self.assertTrue(result1)
		self.assertTrue(result2)
		self.assertTrue(result3)
		self.assertTrue(result4)
		self.assertTrue(result5)
		self.assertTrue(result6)

