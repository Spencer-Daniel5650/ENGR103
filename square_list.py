# Author: Daniel Spencer
# GitHub Username: Spencer-Daniel5650
# Date: 10/23/2023
# Description:The function takes a list of numbers, squares each element, and updates the list in place with these squared values.

def square_list(numbers):
    """
    Replace each value in the list with the square of that value.

    :param numbers: A list of numbers to be squared in-place.
    """
    for i in range(len(numbers)):
        numbers[i] **= 2  # Square the element at index i and update the list

