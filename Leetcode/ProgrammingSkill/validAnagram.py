"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

"""
from collections import Counter  # For counting character frequencies
from operator import truediv


def valid_Anagram(s,t):
    counter_s = Counter(s)
    counter_t = Counter(t)
    print(counter_s)
    print(counter_t)
    return counter_s == counter_t


print(valid_Anagram('anagram','nagaram'))
print(valid_Anagram('rat','cat'))


def isAnagram(s: str, t: str):
    """
    An anagram means both strings contain the exact same characters,
    just possibly in a different order.

    For example:
    - "anagram" and "nagaram" are anagrams (same letters, just rearranged)
    - "rat" and "car" are not (different letters)

    Key concept used: Sorting
    Sorting both strings and comparing them will tell us if they have the same characters.
    """

    # Step 1: Check the lengths first.
    # If the lengths are not the same, they can't be anagrams.
    if len(s) != len(t):
        # Example: "rat" (3 letters) vs "carz" (4 letters) → not possible
        return False

    # Step 2: Sort both strings
    # Sorting puts the letters in a defined order, like alphabetical.
    # For example:
    #   sorted("anagram") -> ['a', 'a', 'a', 'g', 'm', 'n', 'r']
    #   sorted("nagaram") -> ['a', 'a', 'a', 'g', 'm', 'n', 'r']
    sorted_s = sorted(s)
    sorted_t = sorted(t)

    # Debug print to understand what sorting does (for learning purpose)
    print(f"Sorted s: {sorted_s}")
    print(f"Sorted t: {sorted_t}")

    # Step 3: Compare the sorted versions
    # If they are exactly the same, then s and t are anagrams
    return sorted_s == sorted_t


# Test Case 1
# s = "anagram", t = "nagaram" → Should return True
print(isAnagram("anagram", "nagaram"))  # Output: True

# Test Case 2
# s = "rat", t = "car" → Should return False
print(isAnagram("rat", "car"))  # Output: False
