import camel_case
from unittest import TestCase

class TestCamelCase(TestCase):

	def test_first_character_cannot_be_number(self):
		bad_string = '4this is a sentence'

		result = camel_case.check_first_character(bad_string)

		self.assertTrue(result)

