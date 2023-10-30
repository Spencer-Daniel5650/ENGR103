# Author: Daniel Spencer
# GitHub Username: Spencer-Daniel5650
# Date: 10/23/2023
#Description: This is a recursive function that takes two positive integer parameters and returns the product of those numbers

def multiply(a,b):
    if b == 1:
        return a
    return a + multiply(a,b - 1)

