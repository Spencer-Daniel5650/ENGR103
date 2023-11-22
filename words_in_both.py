# Author: Daniel Spencer
# GitHub Username: Spencer-Daniel5650
# Date: 11/21/2023
# Description: This function correctly  returns a set of words that appear in both input strings.

def words_in_both(str1, str2):
    # Convert both strings to lower-case and split into words
    words1 = set(str1.lower().split())
    words2 = set(str2.lower().split())

    # Find the intersection of the two sets of words
    common_words = words1.intersection(words2)

    return common_words


