# Author: Daniel Spencer
# GitHub Username: Spencer-Daniel5650
# Date: 2/27/2024
# Description:

√import time
import random
from functools import wraps
from matplotlib import pyplot as plt

# Decorator to measure sort function execution time
def sort_timer(func):
    @wraps(func)
    def wrapper(arr):
        start_time = time.perf_counter()
        func(arr)
        end_time = time.perf_counter()
        return end_time - start_time
    return wrapper

# Correctly implemented Bubble Sort with sort_timer decorator
@sort_timer
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

#  implement Insertion Sort with sort_timer decorator
@sort_timer
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

# Function to generate lists of sort times for each algorithm
def make_lists_of_sort_times(sort_func1, sort_func2, list_of_lengths):
    times1 = []
    times2 = []
    for n in list_of_lengths:
        # Ensure proper randomization of list
        random_list = [random.randint(1, 10000) for _ in range(n)]
        list_1 = random_list.copy()
        list_2 = random_list.copy()

        time1 = sort_func1(list_1)
        time2 = sort_func2(list_2)

        times1.append(time1)
        times2.append(time2)
    return (times1, times2)

# Function to compare sort times and generate a graph
def compare_sorts(sort_func1, sort_func2):
    # Use a smaller list for initial debugging
    list_of_lengths = [100, 200, 300, 400, 500]  # For quicker testing
    times1, times2 = make_lists_of_sort_times(sort_func1, sort_func2, list_of_lengths)

    plt.figure(figsize=(10, 5))
    plt.plot(list_of_lengths, times1, 'ro--', linewidth=2, markersize=5, label='Bubble Sort')
    plt.plot(list_of_lengths, times2, 'go--', linewidth=2, markersize=5, label='Insertion Sort')
    plt.xlabel('List Length')
    plt.ylabel('Time (seconds)')
    plt.title('Comparison of Bubble Sort and Insertion Sort Performance')
    plt.legend()
    plt.grid(True)
    plt.show()

# Main function to run the comparison
def main():
    compare_sorts(bubble_sort, insertion_sort)

if __name__ == "__main__":
    main()
