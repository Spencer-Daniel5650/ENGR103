# Author: Daniel Spencer
# GitHub Username: Spencer-Daniel5650
# Date: 2/13/2024
# Description:

def list_max(numbers, current_max=None):
    # If current_max is None, this is the first call, so initialize it with the first element of the list
    if current_max is None:
        current_max = numbers[0]

    # Base case: if the list has only one element, compare it with current_max and return the max
    if len(numbers) == 1:
        return max(numbers[0], current_max)

    # Recursive case: compare the first element with current_max and call list_max on the rest of the list
    new_max = max(numbers[0], current_max)
    return list_max(numbers[1:], new_max)

