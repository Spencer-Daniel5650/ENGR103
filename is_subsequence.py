# Author: Daniel Spencer
# GitHub Username: Spencer-Daniel5650
# Date: 2/13/2024
# Description:

def is_subsequence(subseq, seq, subseq_index=0, seq_index=0):
    # Base case 1: If all characters of subseq have been found in seq in order
    if subseq_index == len(subseq):
        return True

    # Base case 2: If seq ends before we find all characters of subseq
    if seq_index == len(seq):
        return False

    # If current character in subseq matches the current character in seq, move to the next character in subseq
    if subseq[subseq_index] == seq[seq_index]:
        return is_subsequence(subseq, seq, subseq_index + 1, seq_index + 1)
    else:
        # If current character in subseq does not match the current character in seq, move to the next character in seq
        return is_subsequence(subseq, seq, subseq_index, seq_index + 1)
