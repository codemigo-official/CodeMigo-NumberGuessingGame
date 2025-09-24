# Number Guessing Game
# Python Project #1 – CodeMigo (Your Coding Buddy)

import random   # import random module to generate random numbers

# Computer selects a random number between 1 and 100
number = random.randint(1, 100)

# Variable to store user's guess (initialized as None)
guess = None  

# Loop runs until the user guesses the correct number
while guess != number:
    # Take input from the user and convert it to an integer
    guess = int(input("Enter your guess (1-100): "))

    # If the guess is smaller than the number
    if guess < number:
        print("Too Low! Try again.")

    # If the guess is greater than the number
    elif guess > number:
        print("Too High! Try again.")

    # If the guess is equal to the number
    else:
        print("🎉 Congratulations! You guessed it right.")
