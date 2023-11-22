# Author: Daniel Spencer
# GitHub Username: Spencer-Daniel5650
# Date: 11/21/2023
# Description: Conuts given letters in a string then tabulates them and displays that value

def count_letters(s):
    # Initialize an empty dictionary to store the count of each letter
    letter_count = {}

    # Iterate over each character in the string
    for char in s:
        # Check if the character is a letter
        if char.isalpha():
            # Convert to upper case
            char = char.upper()
            # Increment the count of the letter in the dictionary
            letter_count[char] = letter_count.get(char, 0) + 1

    return letter_count


