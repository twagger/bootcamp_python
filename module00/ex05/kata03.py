phrase = "The right format"
dashes = 42 - len(phrase)
while dashes > 0:
	print('-', end='')
	dashes -= 1
for letter in phrase:
	print(letter, end='')