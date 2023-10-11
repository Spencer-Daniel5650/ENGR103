# Author: Daniel Spencer
# GitHub Username: Spencer-Daniel5650
# Date: 10/08/2023
# Description: Asks user to input dollar amount under a dollar then prints breakdown of change in quarters, nickels, dimes and pennies

cents = int(input("Please enter an amount in cents less than a dollar:\n"))
# Calculations for each coin
quarters = cents // 25
cents %= 25

dimes = cents // 10
cents %= 10

nickles = cents // 5
cents %= 5

pennies = cents
# Display
print(f"Your change will be:")
print(f"Q: {quarters}")
print(f"D: {dimes}")
print(f"N: {nickles}")
print(f"P: {pennies}")
