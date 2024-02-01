# Author: Daniel Spencer
# GitHub Username: Spencer-Daniel5650
# Date: 1/23/2024
# Description: Creates a binary search and returns an exception when target is not found

class TargetNotFound(Exception):
    """Exception raised when the target is not found in the list."""
    pass

def bin_except(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == target:
            return mid
        if guess < target:
            low = mid + 1
        else:
            high = mid - 1

    raise TargetNotFound(f"Target {target} not found in the list.")


