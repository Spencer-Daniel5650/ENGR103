# Author: Daniel Spencer
# GitHub Username: Spencer-Daniel5650
# Date: 10/17/2023
# Description: asks user to enter integer then begins guessing game
# Ask the user to enter the target integer for guessing

# Ask the user to enter the target integer for guessing
target_integer = int(input("Enter the integer for the player to guess.\n"))

# Initialize variables for the number of tries and user's guess
num_guesses = 0
user_guess = None

# Prompt the user for their initial guess
user_input = input("Enter your guess.\n")
user_guess = int(user_input)

# Start the guessing loop
while True:
    # Increment the number of guesses
    num_guesses += 1

    # Check if the guess is correct
    if user_guess == target_integer:
        if num_guesses == 1:
            print(f"You guessed it in 1 try.")
        else:
            print(f"You guessed it in {num_guesses} tries.")
        break
    elif user_guess > target_integer:
        print("Too high - try again:")
    else:
        print("Too low - try again:")

    # Prompt the user for their next guess
    user_input = input()
    user_guess = int(user_input)
