# Author: Daniel Spencer
# GitHub Username: Spencer-Daniel5650
# Date: 10/17/2023
# Description: Asks user for input of integers then evaluates min and max of input

# Ask the user to enter a positive integer
user_input = input("Please enter a positive integer: ")
num = int(user_input)

# Validate if the input is a positive integer
if num <= 0:
    print("Please enter a valid positive integer.")
else:
    # Initialize a list to store the factors
    factors = []

    # Find the factors of the entered number
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)

    # Print the list of factors
    print("The factors of", num, "are:")
    for factor in factors:
        print(factor)
