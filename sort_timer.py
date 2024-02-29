# Author: Daniel Spencer
# GitHub Username: Spencer-Daniel5650
# Date: 2/27/2024
# Description:

import time
import random
from functools import wraps
from matplotlib import pyplot as plt

# Decorator to measure sort function execution time
def sort_timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        func(*args, **kwargs)
        end_time = time.perf_counter()
        return end_time - start_time
    return wrapper

# Bubble Sort decorated with sort_timer
@sort_timer
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Insertion Sort decorated with sort_timer
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
        random_list = [random.randint(1, 10000) for _ in range(n)]
        list_1 = list(random_list)
        list_2 = list(random_list)

        time1 = sort_func1(list_1)
        time2 = sort_func2(list_2)

        times1.append(time1)
        times2.append(time2)
    return (times1, times2)

# Function to compare sort times and generate a graph
def compare_sorts(sort_func1, sort_func2):
    list_of_lengths = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    times1, times2 = make_lists_of_sort_times(sort_func1, sort_func2, list_of_lengths)

    plt.figure(figsize=(10, 5))
    plt.plot(list_of_lengths, times1, 'ro--', linewidth=2, label='Bubble Sort')
    plt.plot(list_of_lengths, times2, 'go--', linewidth=2, label='Insertion Sort')
    plt.xlabel('List Length')
    plt.ylabel('Time (seconds)')
    plt.title('Comparison of Bubble Sort and Insertion Sort Performance')
    plt.legend(loc='upper left')
    plt.grid(True)
    plt.show()

# Main function to run the comparison
def main():
    compare_sorts(bubble_sort, insertion_sort)

if __name__ == "__main__":
    main()
