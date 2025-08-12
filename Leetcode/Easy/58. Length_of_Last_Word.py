"""
LEETCODE PROBLEM: 58. Length of Last Word
========================================
Problem Statement:
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

Example:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
"""


# Approach 1: Using built-in string methods (Most Pythonic)
def lengthOfLastWord(s):
    """
    ALGORITHM EXPLANATION:
    ================================================================
    Steps:
    1. Remove leading and trailing whitespace using strip()
    2. Split the string into words using split()
    3. Get the last word from the resulting list
    4. Return the length of the last word

    This approach leverages Python's built-in string methods which handle
    multiple spaces and edge cases automatically.

    Learning:
    - String manipulation using strip() and split() methods
    - List indexing with negative indices ([-1] gets last element)
    - Built-in methods often handle edge cases automatically
    - Pythonic approach: using language features to solve problems elegantly
    """

    # Step 1: Remove leading and trailing spaces, then split into words
    # strip() removes spaces from both ends
    # split() splits on any whitespace (spaces, tabs, newlines) and removes empty strings
    words = s.strip().split()

    # Step 2: Get the last word using negative indexing
    # [-1] gets the last element from the list
    last_word = words[-1]

    # Step 3: Return the length of the last word
    return len(last_word)


# Approach 2: Two-pointer technique (More algorithmic approach)
def lengthOfLastWordTwoPointer(s):
    """
    ALGORITHM EXPLANATION:
    ================================================================
    Steps:
    1. Start from the end of the string and skip trailing spaces
    2. Once we find a non-space character, start counting
    3. Count characters until we hit a space or reach the beginning
    4. Return the count

    This approach manually traverses the string from right to left,
    which is more explicit and doesn't use extra space for splitting.

    Learning:
    - Two-pointer/sliding window technique
    - String traversal from right to left
    - Manual character-by-character processing
    - Space-efficient solution (O(1) extra space)
    """

    # Step 1: Initialize pointer at the end of string
    # We'll work backwards to find the last word
    right = len(s) - 1

    # Step 2: Skip trailing spaces by moving pointer left
    # Continue while we have spaces and haven't reached the beginning
    while right >= 0 and s[right] == ' ':
        right -= 1

    # Step 3: Count the length of the last word
    # Initialize counter for word length
    length = 0

    # Count characters until we hit a space or reach the beginning
    while right >= 0 and s[right] != ' ':
        length += 1  # Increment counter for each non-space character
        right -= 1  # Move pointer left to check next character

    # Step 4: Return the length of the last word
    return length
