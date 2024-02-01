# Author: Daniel Spencer
# GitHub Username: Spencer-Daniel5650
# Date: 1/23/2024
# Description: Sorts a list of strings in place, ignoring case sensitivity.

def string_sort(strings):
    """
    Sorts a list of strings in place, ignoring case sensitivity.

    This function implements the insertion sort algorithm, modified to sort strings.
    It sorts the list in a case-insensitive manner but maintains the original case of the strings.

    """
    for i in range(1, len(strings)):
        key = strings[i]
        j = i - 1

        # Compare key with each element on the left of it until an element smaller than it is found
        # For a case insensitive comparison, convert both strings to lowercase
        while j >= 0 and strings[j].lower() > key.lower():
            strings[j + 1] = strings[j]
            j -= 1

        # Place key at after the element just smaller than itself.
        strings[j + 1] = key

