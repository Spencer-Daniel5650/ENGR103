# Author: Daniel Spencer
# GitHub Username: Spencer-Daniel5650
# Date: 10/23/2023
# Description: Finds the median of numbers

def find_median(numbers):
    """
    Find the median of a list of numbers.

    :param numbers: A list of numbers.
    :return: The median of the numbers, or None if the list is empty.
    """
    if not numbers:  # Check if the list is empty
        return None

    sorted_numbers = sorted(numbers)  # Sort the list
    n = len(sorted_numbers)

    if n % 2 == 0:  # Even number of elements
        # The median is the average of the two middle numbers
        return (sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2
    else:  # Odd number of elements
        # The median is the middle number
        return sorted_numbers[n//2]

# Example usage:
# numbers_list = [3, 1, 4, 1, 5, 9, 2]
# print(find_median(numbers_list))
