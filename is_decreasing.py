# Author: Daniel Spencer
# GitHub Username: Spencer-Daniel5650
# Date: 2/13/2024
# Description:

def is_decreasing(numbers, index=0):
    # Base case: if we've reached the end of the list, return True
    if index == len(numbers) - 1:
        return True

    # Check if the current element is strictly greater than the next element
    if numbers[index] <= numbers[index + 1]:
        return False

    # Recursive case: move to the next pair of elements
    return is_decreasing(numbers, index + 1)

