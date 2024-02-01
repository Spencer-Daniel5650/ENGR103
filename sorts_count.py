# Author: Daniel Spencer
# GitHub Username: Spencer-Daniel5650
# Date: 1/23/2024
# Description: unction sorts a list using the bubble
# sort algorithm and returns the number of element comparisons and swaps made

def bubble_count(lst):
    """
        Perform bubble sort on a list and count the number of comparisons and exchanges made.
        Returns:
        tuple: A tuple containing two integers - the number of comparisons and the number of exchanges.
        """
    n = len(lst)
    comparisons = 0
    exchanges = 0

    for i in range(n):
        for j in range(0, n-i-1):
            comparisons += 1
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                exchanges += 1

    return comparisons, exchanges

def insertion_count(lst):
    n = len(lst)
    comparisons = 0
    exchanges = 0

    for i in range(1, n):
        key = lst[i]
        j = i-1
        while j >= 0 and key < lst[j]:
            comparisons += 1
            lst[j+1] = lst[j]
            j -= 1
            exchanges += 1
        if j >= 0:
            comparisons += 1  # For the last comparison where key >= lst[j]
        lst[j+1] = key

    return comparisons, exchanges
