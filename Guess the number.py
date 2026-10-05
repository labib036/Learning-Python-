import random
secNumber =random.randint(1,20)
print("I'm thinking of a number between 1 and 20")

for guesstaken in range (1,10):
	print("Guess a number")
	guess =int(input())

	if guess < secNumber:
		print("Your guess is too low")
	elif guess> secNumber:
		print("You guess is too high")
	else:
		break
if guess == secNumber:
	print("Good Job! You gussed my number in " +str(guesstaken)  + " guesses ")
else: 
	print("you couldn't guess my number")		