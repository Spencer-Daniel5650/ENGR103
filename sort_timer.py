# Author: Daniel Spencer
# GitHub Username: Spencer-Daniel5650
# Date: 2/27/2024
# Description:

import time
import random
from matplotlib import pyplot

# Decorator function to measure the time taken by a function to run
def sort_timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        func(*args, **kwargs)
        end_time = time.perf_counter()
        return end_time - start_time
    return wrapper

# Bubble sort algorithm
@sort_timer
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Insertion sort algorithm
@sort_timer
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Function to compare sorting algorithms and generate a graph
def compare_sorts(bubble_sort_func, insertion_sort_func):
    sizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    bubble_times = []
    insertion_times = []

    for size in sizes:
        data = [random.randint(1, 10000) for _ in range(size)]

        # Bubble Sort
        bubble_time = bubble_sort_func(data.copy())
        bubble_times.append(bubble_time)

        # Insertion Sort
        insertion_time = insertion_sort_func(data.copy())
        insertion_times.append(insertion_time)

    # Plotting the results
    pyplot.plot(sizes, bubble_times, 'ro--', label='Bubble Sort', linewidth=2)
    pyplot.plot(sizes, insertion_times, 'go--', label='Insertion Sort', linewidth=2)
    pyplot.xlabel('List Size')
    pyplot.ylabel('Time (seconds)')
    pyplot.title('Comparison of Bubble Sort and Insertion Sort')
    pyplot.legend()
    pyplot.show()