import sys

result = ''
first = True
for arg in sys.argv:
	if first:
		first = False
	else:
		result += arg + ' '
result = result[:-1]
result = result[::-1]
for letter in result:
	if letter.islower():
		letter = letter.upper()
	elif letter.isupper():
		letter = letter.lower()
	print(letter, end='')
if result != '':
	print()