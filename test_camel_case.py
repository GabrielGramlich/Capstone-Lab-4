import camel_case
from unittest import TestCase

class TestCamelCase(TestCase):

	def test_first_character_cannot_be_number(self):
		bad_string = '4this is a sentence'

		result = camel_case.invalid_sentence(bad_string)

		self.assertTrue(result)


	def test_first_character_can_be_string(self):
		good_string = 'this is a sentence'

		result = camel_case.invalid_sentence(good_string)

		self.assertFalse(result)


	def test_not_blank(self):
		bad_string = ''

		result = camel_case.invalid_sentence(bad_string)

		self.assertTrue(result)


	def test_remove_special_characters(self):
		bad_string = '/this, sen#ten\'ce is .valid\\'
		good_string = 'this sentence is valid'

		result = camel_case.remove_special_characters(bad_string, False)

		self.assertEqual(result, good_string)


	def test_convert_strings_with_different_cases(self):
		good_string = 'Word'
		original_string = 'wOrD'

		result = camel_case.convert_word_to_title_case(original_string)

		self.assertEqual(result, good_string)


	def test_convert_strings_with_different_cases_first_character_numeric(self):
		good_string = '1gloo'
		original_string = '1gLoO'

		result = camel_case.convert_word_to_title_case(original_string)

		self.assertEqual(result, good_string)


	def test_normal_sentence_converts_to_camel_case(self):
		camel_case_string = 'thisIsASentence'
		original_string1 = 'This is a sentence'
		original_string2 = 'THIS IS A SENTENCE'

		result1 = camel_case.convert_sentence(original_string1)
		result2 = camel_case.convert_sentence(original_string2)

		self.assertEqual(result1, camel_case_string)
		self.assertEqual(result2, camel_case_string)


	def test_normal_sentence_converts_to_camel_case_with_numbers(self):
		camel_case_string = 'c4nY0uR34d13377h0'
		leet_string = 'C4n y0u r34d 1337 7h0'

		result = camel_case.convert_sentence(leet_string)

		self.assertEqual(result, camel_case_string)

