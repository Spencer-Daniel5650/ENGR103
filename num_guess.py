# Author: Daniel Spencer
# GitHub Username: Spencer-Daniel5650
# Date: 10/17/2023
# Description:
# Ask the user to enter the target integer for guessing
target_integer = int(input("Enter the integer for the player to guess.\n"))

# Initialize variables for the number of tries and user's guess
num_guesses = 0
user_guess = None

# Start the guessing loop
while True:
    # Prompt the user for their guess
    user_input = input("Enter your guess.\n")
    user_guess = int(user_input)

    # number of guesses
    num_guesses += 1

    # Check if the guess is correct
    if user_guess == target_integer:
        if num_guesses == 1:
            print(f"You guessed it in 1 try.")
        else:
            print(f"You guessed it in {num_guesses} tries.")
        break
    elif user_guess > target_integer:
        print("too high - try again:")
    else:
        print("too low - try again:")
