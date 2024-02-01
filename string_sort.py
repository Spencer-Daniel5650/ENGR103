# Author: Daniel Spencer
# GitHub Username: Spencer-Daniel5650
# Date: 1/23/2024
# Description: Sorts a list of strings in place, ignoring case sensitivity.

# Function to do insertion sort
def insertionSort(arr):

    # Start from the second element and go till the end
    for i in range(1, len(arr)):

        key = arr[i]	# Current element

        j = i-1		# Index just before the current i

	# Try till the first element
	# Compare element at j and element at i
	# Copy the j'th element if it is smaller than the i'th

        # here we will compare string ignoring-case. (Convert it to lower-case)
        while j >= 0 and key.lower() < arr[j].lower() :
                arr[j + 1] = arr[j]
                j -= 1

	# Copy the curernt i'th element
        arr[j + 1] = key


# Driver code

# Set some randome values in the list
arr = ["apple", "maRker", "marble", "zebra", "ball"]

insertionSort(arr)

