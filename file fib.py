# Author: Daniel Spencer
# GitHub Username: Spencer-Daniel5650
# Date: 10/23/2023
# Description: Creates a function named fib that takes positive integer and returns the numerical location it resides in the fibonacci sequence.

def hailstone(n):
    if n == 1:
        return 0

    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1

    return steps

# Test the function with different values for n
n_values = [1000, 3, 27, 7]  # Add more values as needed

for n in n_values:
    steps = hailstone(n)
    print(f"Steps to reach 1 for n = {n}: {steps}")


