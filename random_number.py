import random
playing = True
number = str(random.randint(0,9))
while playing:
    guess = input("Guess a number between 0 and 9: \n")
    if guess == number:
        print("You guessed it!")
        break
    else:
        print("Try again!\n")