import sys

def filter_punct(word: str):
	
	return word		

result = []
puncts = '.,:;!?()[]'
nb_params = len(sys.argv)
if nb_params > 3 or nb_params < 3:
	print("ERROR")
	exit()
if not sys.argv[2].isnumeric() or not isinstance(sys.argv[1], str):
	print("ERROR")
	exit()
wlist = sys.argv[1].split(' ')
for word in wlist:
	for punct in puncts:
		word = word.replace(punct, '')
	if len(word) >= int(sys.argv[2]):
		result.append(word)
print(result)