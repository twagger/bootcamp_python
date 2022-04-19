import sys
import string 

def text_analyzer(text=''):
	"""This function counts the number of upper characters, lower characters,
	punctuation and spaces in a given text."""
	if type(text) != str:
		print("AssertionError : argument is not a string")
	else:
		while len(text) == 0:
			text = raw_input("What is the text to analyze?\n")
		print("The text contains " + str(len(text)) + " character(s):")
		result = [0, 0, 0, 0]
		for letter in text:
			if letter.isupper():
				result[0] += 1
			if letter.islower():
				result[1] += 1
			if letter in string.punctuation:
				result[2] += 1
			if letter.isspace():
				result[3] += 1
		print("- " + str(result[0]) + " upper letter(s)")
		print("- " + str(result[1]) + " lower letter(s)")
		print("- " + str(result[2]) + " punctuation mark(s)")
		print("- " + str(result[3]) + " space(s)")