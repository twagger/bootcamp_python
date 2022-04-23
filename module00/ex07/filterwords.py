import sys
import string

def clear_punctuation(word):
	result = ""
	for letter in word:
		if letter not in string.punctuation:
			result += letter
	return result

if len(sys.argv) != 3:
	print("Usage: python filterwords.py [string] [int]")
else:
	words = sys.argv[1].split(' ')
	words_no_punct = [clear_punctuation(word) for word in words]
	result = [word for word in words_no_punct if len(word) > int(sys.argv[2])]
	print(result)