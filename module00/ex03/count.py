def text_analyzer(text: str):
	total = 0
	upper = 0
	lower = 0
	punct = 0
	space = 0
	marks = '.,:;!?()[]'
	for letter in text:
		total += 1
		if letter.isupper():
			upper += 1
		if letter.islower():
			lower += 1
		if letter.isspace():
			space += 1
		if marks.find(letter) > -1:
			punct += 1
	print("The text contains " + str(total) + " characters:")
	print("- " + str(upper) + " upper letters")
	print("- " + str(lower) + " lower letters")
	print("- " + str(punct) + " punctuation marks")
	print("- " + str(space) + " spaces")