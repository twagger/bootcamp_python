import sys

# check arguments
if len(sys.argv) == 1:
	print("Usage: python exec.py [Arguments] ...")
else:
	# build a unique string
	unique = sys.argv[1]
	for w in sys.argv[2:]:
		unique += ' ' + w
	# create the result string
	result = ''
	for i in range(len(unique) - 1, -1, -1):
		if unique[i].islower():
			result += unique[i].upper()
		elif unique[i].isupper():
			result += unique[i].lower()
		else:
			result += unique[i]
	print(result)