# Author: Daniel Spencer
# GitHub Username: Spencer-Daniel5650
# Date: 2/27/2024
# Description:

import time
import random
from functools import wraps
from matplotlib import pyplot as plt

def sort_timer(func):
    """
    Decorator function to time the execution of a decorated function.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        return elapsed_time
    return wrapper

@sort_timer
def bubble_sort(arr):
    """
    Bubble sort algorithm.
    """
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

@sort_timer
def insertion_sort(arr):
    """
    Insertion sort algorithm.
    """
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def make_lists_of_sort_times(sort_func1, sort_func2, lengths):
    """
    Generate lists of sort times for two sort algorithms.
    """
    bubble_sort_times = []
    insertion_sort_times = []

    for length in lengths:
        # Generate random list of length 'length'
        random_list = [random.randint(1, 10000) for _ in range(length)]

        # Create copies of the random list for each sort function
        list1 = random_list.copy()
        list2 = random_list.copy()

        # Time bubble sort and insertion sort
        bubble_sort_time = sort_func1(list1)
        insertion_sort_time = sort_func2(list2)

        # Append the sort times to the respective lists
        bubble_sort_times.append(bubble_sort_time)
        insertion_sort_times.append(insertion_sort_time)

    return bubble_sort_times, insertion_sort_times

def compare_sorts(sort_func1, sort_func2):
    """
    Compare the execution times of two sort algorithms and generate a graph.
    """
    lengths = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

    # Get the lists of sort times
    bubble_sort_times, insertion_sort_times = make_lists_of_sort_times(sort_func1, sort_func2, lengths)

    # Plot the graph
    plt.plot(lengths, bubble_sort_times, 'ro--', linewidth=2, label='Bubble Sort')
    plt.plot(lengths, insertion_sort_times, 'go--', linewidth=2, label='Insertion Sort')
    plt.xlabel("Number of Elements")
    plt.ylabel("Time (seconds)")
    plt.legend(loc='upper left')
    plt.show()

# Generate the graph
compare_sorts(bubble_sort, insertion_sort)