# Author: Daniel Spencer
# GitHub Username: Spencer-Daniel5650
# Date: 1/23/2024
# Description: unction sorts a list using the bubble
# sort algorithm and returns the number of element comparisons and swaps made

def insertion_count(a_list):
    """
    Perform insertion sort on a_list and return a tuple (comparisons, exchanges)
    where comparisons is the number of comparisons between elements and
    exchanges is the number of times elements are inserted in a different position.
    """
    comparisons = 0
    exchanges = 0
    n = len(a_list)

    for i in range(1, n):
        key = a_list[i]
        j = i - 1

        # Perform comparisons and shift elements of a_list[0..i-1]
        while j >= 0:
            if a_list[j] > key:
                comparisons += 1
                a_list[j + 1] = a_list[j]
                exchanges += 1
                j -= 1
            else:
                comparisons += 1
                break
        a_list[j + 1] = key

    return comparisons, exchanges
