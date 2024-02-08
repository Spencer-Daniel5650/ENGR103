# Author: Daniel Spencer
# GitHub Username: Spencer-Daniel5650
# Date: 2/7/2024
# Description: Reads a list of numbers from a file, sums them, and writes the sum to 'sum.txt'.

def file_sum(filename):
    """
    This function reads each line of the input file assuming each line contains a single
    number (either integer or floating-point). It converts these lines to numbers, sums them,
    and writes the total sum to a file named 'sum.txt'. If a line cannot be converted to a number,
    it skips that line and prints a warning message. The function does not return any value.
    """

    # Initialize sum
    total_sum = 0

    # Open the file and read numbers line by line
    with open(filename, 'r') as file:
        for line in file:
            # Convert each line to a float and add it to the total sum
            try:
                number = float(line.strip())
                total_sum += number
            except ValueError:
                # Handle the case where the line is not a valid number
                print(f"Skipping invalid line: {line.strip()}")

    # Write the sum to sum.txt
    with open('sum.txt', 'w') as output_file:
        output_file.write(str(total_sum))

# Example usage
# file_sum('numbers.txt')



