# Import the random module into the script
import random

# Define a method that accepts user inputs and compares this against a randomly
# generated number in a range
def guessingGame (minGuess, maxGuess):
    guessLimit = 10
    guesses = 0
    guessesLeft = guessLimit

    # Generates a random number that user must guess
    secretNumber = random.randint(minGuess, maxGuess)

    # Will remain true while user has not used up their guesses
    while guesses < guessLimit:
        userGuess = int(input("Please guess a number between {} and {}: " .format(minGuess, maxGuess)))

        # Check passed if guess matched random number
        if userGuess == secretNumber:
            print("Correct! The number I was thinking of WAS {}" .format(secretNumber))
            break

        # Provides the user a hint in high guess case
        elif userGuess > secretNumber:
            guesses += 1
            guessesLeft -= 1
            print("You guessed too high! You have {} guesses left." .format(guessesLeft))
            continue

	# provides the user a hing in low guess case
        else:
            guesses += 1
            guessesLeft -= 1
            print("You guessed too low! You have {} guesses left." .format(guessesLeft))
            continue

    # Is printed if the user runs out of guesses. Prints the random number	
    else:
        print("You are out of guesses. The number was {}" .format(secretNumber))
        

guessingGame (0, 100)
