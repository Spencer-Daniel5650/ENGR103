# Author: Daniel Spencer
# GitHub Username: Spencer-Daniel5650
# Date: 10/23/2023
# Description:hat reverses the order of elements in a list without using slicing or the built-in reverse function,

def reverse_list(lst):
    """
    Reverse the order of elements in a given list in-place.

    :param lst: A list to be reversed.
    """
    i = 0  # Start index
    j = len(lst) - 1  # End index

    while i < j:
        # Swap elements
        lst[i], lst[j] = lst[j], lst[i]

        # Move towards the middle
        i += 1
        j -= 1

