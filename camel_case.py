def main():
	display_banner()
	sentence = get_sentence()
	converted_sentence = convert_sentence(sentence)
	print_converted_sentence(converted_sentence)


def display_banner():
	""" Display program name in banner """
	# This code was written by Clara James
	msg = 'AWSOME camelCaseGenerator PROGRAM'
	stars = '*' * len(msg)
	print(f'\n {stars} \n {msg} \n {stars}\n')


def get_sentence():
	print()
	sentence = get_clean_sentence()
	while invalid_sentence(sentence):
		sentence = get_clean_sentence()

	return sentence


def get_clean_sentence():
	sentence = input('Please input a sentence to convert to a camelCase variable. ')
	clean_sentence = remove_special_characters(sentence)

	return clean_sentence


def remove_special_characters(sentence, bad):
	bad_characters = ['#', '/', ',', '\'', '\\', '.']
	for character in bad_characters:
		while character in sentence:
			sentence = sentence.replace(character, '')

	return sentence


def invalid_sentence(sentence):
	invalid_character = validate_first_character(sentence)
	invalid_length = is_blank(sentence)

	return invalid_character or invalid_length


def validate_first_character(sentence):
	try:
		int(sentence[0:1])
		return True
	return False


def is_blank(sentence):
	if len(sentence) > 0:
		return False
	return True


def convert_sentence(sentence):
	words = sentence.split()
	converted_sentence = ''
	for i in range(len(words)):
		if i == 0:
			converted_sentence = converted_sentence + words[i].lower()
		else:
			word = words[i]
			converted_word = convert_word_to_title_case(word)
			converted_sentence = converted_sentence + converted_word

	return converted_sentence


def convert_word_to_title_case(word):
	converted_word = ''
	for letter in range(len(word)):
		if letter == 0:
			converted_word = word[letter:letter+1].upper()
		else:
			converted_word = converted_word + word[letter:letter+1].lower()

	return converted_word


def print_converted_sentence(sentence):
	print('\nHere is your sentence converted to camel case: {0}'.format(sentence))
	print()


if __name__ == '__main__':
	main()
