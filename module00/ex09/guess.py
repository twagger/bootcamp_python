import random

print("""\
This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!
""")
guess = ''
num = random.randint(1, 99)
trials = 0
while 1:
	guess = input("What's your guess between 1 and 99?\n>> ")
	if guess == 'exit':
		print("Goodbye!")
		break
	trials += 1
	try:
		int(guess)
	except ValueError:
		print("That's not a number.")
		continue
	if int(guess) > num:
		print("Too high!")
	elif int(guess) < num:
		print("Too low!")
	else:
		if num == 42:
			print("The answer to the ultimate question of life, the universe and everything is 42.")
		if trials == 1:
			print("Congratulations! You got it on your first try!")
			break
		else:
			print("Congratulations, you've got it !")
			print("You won in {} attempts!".format(trials))
			break