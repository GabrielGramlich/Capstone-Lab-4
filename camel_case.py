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
	sentence = input('Please input a sentence to convert to a camelCase variable. ')
	while validate_characters(sentence):
		print('Are you kitten me right meow? You can\'t name a variable that! Try again.')
		sentence = input('Please input a sentence to convert to camelCase. ')

	return sentence


def validate_characters(sentence):
	bad = check_first_character(sentence)
	bad = check_special_characters(sentence, bad)

	return bad


def check_first_character(sentence):
	try:
		int(sentence[0:1])
		return True
	except:
		return False


def check_special_characters(sentence, bad):
	bad_characters = ['#', '/', ',', '\'', '\\', '.']
	for character in bad_characters:
		if sentence.find(character) != -1:
			bad = True

	return bad


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


main()
