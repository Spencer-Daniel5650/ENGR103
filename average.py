# Author: Daniel Spencer
# GitHub Username: Spencer-Daniel5650
# Date: 10/01/2023
# Discription: Asks user to input five numbers then prints the mean of said numbers




# Initialize a variable to store the sum of the numbers
total = 0

# Ask user for five numbers
print("Please enter five numbers:")
for i in range(5):
    # Use a try-except block to handle invalid input
    try:
        number = float(input())
        total += number
    except ValueError:
        print("Invalid input, Please enter a number.")

# Calculate the average
average = total / 5

# Print the average
print("The average of those numbers is:")
print(average)
