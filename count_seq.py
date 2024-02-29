# Author: Daniel Spencer
# GitHub Username: Spencer-Daniel5650
# Date: 2/13/2024
# Description: Generate an infinite sequence
def count_seq():
    """
    Generate an infinite sequence where each term is derived by describing the count of digits
    in the previous term.

    """
    term = "1"  # The sequence technically starts by describing "1" as "one 2", but we'll start from generating "2".
    while True:
        if term == "1":  # Special case for the very first term.
            term = "2"
        else:
            new_term = ""
            count = 1
            # Loop through the term, counting consecutive numbers.
            for i in range(1, len(term)):
                if term[i] == term[i-1]:
                    count += 1
                else:
                    new_term += str(count) + term[i-1]
                    count = 1
            new_term += str(count) + term[-1]
            term = new_term
        yield term
