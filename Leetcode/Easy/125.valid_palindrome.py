"""
LEETCODE PROBLEM: 125. Valid Palindrome
========================================
Problem Statement:
A phrase is a palindrome if, after converting all uppercase letters into lowercase 
letters and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""


# Approach to solve the problem
def isPalindrome(s):
    """
    ALGORITHM EXPLANATION:
    ================================================================
    Steps:
    1. Use two pointers: one at the beginning (left) and one at the end (right)
    2. Move pointers towards each other, skipping non-alphanumeric characters
    3. Compare characters at both pointers (after converting to lowercase)
    4. If characters don't match, return False
    5. If pointers meet or cross, we've checked all valid characters - return True

    Learning: 
    - Two-pointer technique for string problems
    - Character validation using isalnum() method
    - Case-insensitive comparison using lower() method
    - Efficient O(1) space solution without creating new strings
    - Understanding palindrome properties and optimization techniques
    """

    # Initialize two pointers at the beginning and end of string
    left = 0  # Left pointer starts at index 0
    right = len(s) - 1  # Right pointer starts at last index

    # Continue until pointers meet or cross each other
    while left < right:

        # Skip non-alphanumeric characters from the left side
        # Keep moving left pointer until we find a valid character
        while left < right and not s[left].isalnum():
            left += 1

        # Skip non-alphanumeric characters from the right side
        # Keep moving right pointer until we find a valid character
        while left < right and not s[right].isalnum():
            right -= 1

        # Now both pointers point to alphanumeric characters
        # Compare them after converting to lowercase for case-insensitive comparison
        if s[left].lower() != s[right].lower():
            # Characters don't match, so it's not a palindrome
            return False

        # Characters match, move both pointers towards center
        left += 1  # Move left pointer forward
        right -= 1  # Move right pointer backward

    # If we've checked all characters and none mismatched, it's a palindrome
    return True