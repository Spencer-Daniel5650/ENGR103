# Author: Daniel Spencer
# GitHub Username: Spencer-Daniel5650
# Date: 10/23/2023
#Description: creates a hailstone sequence based off of a function named hailstone that uses initail positive integer
def hailstone(initial_number):
    if initial_number == 1:
        return 0

    steps = 0
    while initial_number != 1:
        if initial_number % 2 == 0:
            initial_number = initial_number // 2
        else:
            initial_number = 3 * initial_number + 1
        steps += 1

    return steps

