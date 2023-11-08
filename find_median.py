# Author: Daniel Spencer
# GitHub Username: Spencer-Daniel5650
# Date: 11/06/2023
# Description: The find_median function sorts a given list of numbers and returns the median value, or None if the list is empty.

def find_median(numbers):
    """
    Sort the list and return the median of the numbers.
    If the list is empty, return None.
    """
    if not numbers:  # If the list is empty
        return None

    numbers.sort()  # Sort the list in place
    n = len(numbers)
    middle = n // 2  # Find the middle index

    if n % 2 == 0:  # If the list has an even number of elements
        # The median is the average of the two middle numbers
        return (numbers[middle - 1] + numbers[middle]) / 2
    else:  # If the list has an odd number of elements
        # The median is the middle number
        return numbers[middle]

# Example usage:
values = [13, 7, -3, 82, 4]
result = find_median(values)  # result should be 7
