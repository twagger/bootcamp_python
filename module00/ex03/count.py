import sys

def text_analyser(str):
	:

# check arguments
if len(sys.argv) <= 1:
	print("Usage: python whois.py [Argument]")
elif len(sys.argv) >= 3:
	print("AssertionError: more than one argument are provided")
else:
	if sys.argv[1].isdigit() == False:
		print("AssertionError: argument is not an integer")
	elif int(sys.argv[1]) == 0:
		print("I'm Zero.")
	elif int(sys.argv[1]) % 2 == 0:
		print("I'm Even.")
	else:
		print("I'm Odd.")