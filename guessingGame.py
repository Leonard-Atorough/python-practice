import random

def guessingGame (minGuess, maxGuess):
    guessLimit = 10
    guesses = 0
    guessesLeft = guessLimit
    
    secretNumber = random.randint(minGuess, maxGuess)
    
    while guesses < guessLimit:
        userGuess = int(input("Please guess a number between {} and {}: " .format(minGuess, maxGuess)))
        
        if userGuess == secretNumber:
            print("Correct! The number I was thinking of WAS {}" .format(secretNumber))
            break

        elif userGuess > secretNumber:
            guesses += 1
            guessesLeft -= 1
            print("You guessed too high! You have {} guesses left." .format(guessesLeft))
            continue
	
        else:
            guesses += 1
            guessesLeft -= 1
            print("You guessed too low! You have {} guesses left." .format(guessesLeft))
            continue
	
    else:
        print("You are out of guesses. The number was {}" .format(secretNumber))

guessingGame (0, 100)
