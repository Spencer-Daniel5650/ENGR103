# Author: Daniel Spencer
# GitHub Username: Spencer-Daniel5650
# Date: 10/01/2023
# Description: Asks user to input temperature in celsius then converts to fahrenheit

# Prompt input
celsius = float(input("Please enter a Celsius temperature:\n"))
#Convert C to F
fahrenheit = (9/5) * celsius + 32
print(f"The equivalent Fahrenheit temperature is:\n{fahrenheit}")