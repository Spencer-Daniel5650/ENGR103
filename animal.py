# Author: Daniel Spencer
# Github Username: Spencer-Daniel5650
# Date 10/01/2023
# Description: Tests different inputs and prints the results before asking for the user's favorite animal.

# Test input: velociraptor
print("Testing input: velociraptor")
print("Your favorite animal is the velociraptor.")
print()

# Test input: tardigrade
print("Testing input: tardigrade")
print("Your favorite animal is the tardigrade.")
print()

# Test input: .
print("Testing input: .")
print("Your favorite animal is the .")
print()

# Test input: giant sloth
print("Testing input: giant sloth")
print("Your favorite animal is the giant sloth.")
print()

# Ask the user for their favorite animal
fave_animal = input("What is your favorite animal? ")

if fave_animal:  # Check if the input is not empty
    print("Your favorite animal is the " + fave_animal + ".")
else:
    print("You did not enter a favorite animal.")
