# Author: Daniel Spencer
# GitHub Username: Spencer-Daniel5650
# Date: 10/23/2023
# Description: Creates a function named fib that takes positive integer and returns the numerical location it resides in the fibonacci sequence.

import unittest
def fib(n):
    if n <= 0:
        return None  # Handle invalid input

    if n == 1 or n == 2:
        return 1  # Base case for the first two Fibonacci numbers

    fib_prev = 1  # Initialize the previous Fibonacci number to 1
    fib_curr = 1  # Initialize the current Fibonacci number to 1

    for i in range(3, n + 1):
        fib_next = fib_prev + fib_curr  # Calculate the next Fibonacci number
        fib_prev, fib_curr = fib_curr, fib_next  # Update previous and current Fibonacci numbers

    return fib_curr  # Return the Fibonacci number at position n

# Example usage:
term = fib(10)
print(term)  # Output will be 55
