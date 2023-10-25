# Author: Daniel Spencer
# GitHub Username: Spencer-Daniel5650
# Date: 10/23/2023
# Description: Creates a function named fib that takes positive integer and returns the numerical location it resides in the fibonacci sequence.

def fib(n):
    fib_prev = 1
    fib_current = 1

    if n == 1 or n == 2:
        return 1
    else:
        for _ in range(3, n + 1):
            fib_next = fib_prev + fib_current
            fib_prev, fib_current = fib_current, fib_next
        return fib_current
n = 10
fib(n)





