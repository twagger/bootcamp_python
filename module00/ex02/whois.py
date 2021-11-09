import sys

if len(sys.argv) > 2:
	print('ERROR')
elif len(sys.argv) < 2:
	print('ERROR')
elif sys.argv[1].strip('-').isdecimal() == False:
	print('ERROR')
elif int(sys.argv[1]) == 0:
	print("I'm  Zero.")
elif int(sys.argv[1]) % 2 == 0:
	print("I'm  Even.")
elif int(sys.argv[1]) % 2 == 1:
	print("I'm  Odd.")