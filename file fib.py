# Author: Daniel Spencer
# GitHub Username: Spencer-Daniel5650
# Date: 10/23/2023
# Description: Creates a function named fib that takes positive integer and returns the numerical location it resides in the fibonacci sequence.

import unittest
def fib(n):
    if n <= 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        fib_prev = 1
        fib_current = 1
        for _ in range(3, n + 1):
            fib_next = fib_prev + fib_current
            fib_prev, fib_current = fib_current, fib_next
        return fib_current

class TestFib(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(3), 2)
        self.assertEqual(fib(10), 55)

if __name__ == "__main__":
    unittest.main()