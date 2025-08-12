"""
LEETCODE PROBLEM: 28. Find the Index of the First Occurrence in a String
========================================
Problem Statement:
Given two strings needle and haystack, return the index of the first occurrence
of needle in haystack, or -1 if needle is not part of haystack.

Example:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6. The first occurrence is at index 0.

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
"""


# Approach 1: Built-in Method (Easiest for beginners)
def strStr_builtin(haystack, needle):
    """
    Using Python's built-in find() method
    Time Complexity: O(n*m) where n = len(haystack), m = len(needle)
    Space Complexity: O(1)
    """
    # Handle edge case: empty needle should return 0
    if not needle:
        return 0

    # Use built-in find method which returns -1 if not found
    return haystack.find(needle)


# Approach 2: Sliding Window (Manual Implementation)
def strStr_sliding_window(haystack, needle):
    """
    Manual sliding window approach - good for understanding the logic
    Time Complexity: O(n*m) where n = len(haystack), m = len(needle)
    Space Complexity: O(1)
    """
    # Handle edge cases
    if not needle:  # Empty needle
        return 0
    if len(needle) > len(haystack):  # Needle longer than haystack
        return -1

    # Get lengths for easier reference
    haystack_len = len(haystack)
    needle_len = len(needle)

    # Slide through haystack, checking each possible starting position
    # We only need to check up to (haystack_len - needle_len) positions
    for i in range(haystack_len - needle_len + 1):
        # Check if substring starting at position i matches needle
        if haystack[i:i + needle_len] == needle:
            return i

    # If we've checked all positions and found no match
    return -1


# Approach 3: Character-by-Character Comparison (Most Educational)
def strStr_char_by_char(haystack, needle):
    """
    Character by character comparison - helps understand string matching logic
    Time Complexity: O(n*m) where n = len(haystack), m = len(needle)
    Space Complexity: O(1)
    """
    # Handle edge cases
    if not needle:
        return 0
    if len(needle) > len(haystack):
        return -1

    haystack_len = len(haystack)
    needle_len = len(needle)

    # Try each starting position in haystack
    for start in range(haystack_len - needle_len + 1):
        # Check if all characters match starting from this position
        match_found = True

        # Compare each character of needle with haystack
        for j in range(needle_len):
            if haystack[start + j] != needle[j]:
                match_found = False
                break  # No need to check remaining characters

        # If all characters matched, we found our answer
        if match_found:
            return start

    # No match found
    return -1


"""
ALGORITHM EXPLANATION:
================================================================
Steps:
1. Handle Edge Cases:
   - If needle is empty, return 0 (by convention)
   - If needle is longer than haystack, return -1 (impossible to find)

2. Sliding Window Approach:
   - Start from index 0 of haystack
   - At each position, check if substring of length needle_len matches needle
   - If match found, return current index
   - If no match, move to next position
   - Continue until we've checked all valid starting positions

3. Character-by-Character Approach:
   - For each valid starting position in haystack
   - Compare each character of needle with corresponding character in haystack
   - If all characters match, return starting position
   - If any character doesn't match, try next starting position

Key Insights:
- We only need to check positions 0 to (haystack_len - needle_len)
- Once we find a mismatch, we can immediately move to next starting position
- String slicing in Python creates new objects, so character comparison can be more efficient

Learning Points:
================================================================
1. **String Indexing**: Understanding how to access characters at specific positions
2. **Bounds Checking**: Ensuring we don't go out of array/string bounds
3. **Early Termination**: Breaking loops when we find what we're looking for
4. **Edge Case Handling**: Always consider empty inputs and boundary conditions
5. **Multiple Approaches**: Same problem can be solved in different ways with trade-offs
6. **Built-in vs Custom**: When to use built-in methods vs implementing your own logic

Implementation Tips:
- Always test with edge cases: empty strings, single characters, no matches
- Consider time/space complexity trade-offs between different approaches
- Built-in methods are usually optimized but custom implementation helps understanding
- String slicing (haystack[i:j]) is convenient but creates new string objects
"""
