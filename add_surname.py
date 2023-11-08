# Author: Daniel Spencer
# GitHub Username: Spencer-Daniel5650
# Date: 11/06/2023
# Description: The add_surname function creates a new list of names by appending the surname "Kardashian" to each first name from the input list that starts with the letter "K".

def add_surname(first_names):
    """
    Return a list of names that start with 'K' with 'Kardashian' added as the surname.
    """
    return [f"{name} Kardashian" for name in first_names if name.startswith('K')]
