# Author: Daniel Spencer
# GitHub Username: Spencer-Daniel5650
# Date: 10/17/2023
# Description: Asks user for input of integers then evaluates min and max of input

# Ask the user how many integers they would like to enter
num_integers = int(input("How many integers would you like to enter?\n"))

# Initialize variables to hold the minimum and maximum values
integers = []

# Prompt the user to enter the integers
print(f"Please enter {num_integers} integers:")
for i in range(num_integers):
    num = int(input())
    integers.append(num)

# Calculate the minimum and maximum values
min_value = min(integers)
max_value = max(integers)

# Display the minimum and maximum values
print(f"min: {min_value}")
print(f"max: {max_value}")
