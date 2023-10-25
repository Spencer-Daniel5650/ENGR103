# Author: Daniel Spencer
# GitHub Username: Spencer-Daniel5650
# Date: 10/23/2023
#Description: creates a hailstone sequence based off of a function named hailstone that uses initail positive integer

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

# Test the function
answer = hailstone(1000)
print(answer)
