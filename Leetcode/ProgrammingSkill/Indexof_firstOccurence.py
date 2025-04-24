"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack
Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
"""
from operator import index


def strStr(haystack: str, needle: str) -> int:
    """
    Return the index of the first occurrence of `needle` in `haystack`, or -1 if not found.
    """

    # 1. Quick check: if `needle` is empty, by convention we return 0
    #    (every string contains the empty string at index 0).
    if not needle:
        return 0

    # 2. Use Python's highly optimized substring membership test (`in`),
    #    which internally uses a fast search algorithm (often Boyer–Moore–Horspool or similar).
    #    This runs in O(n + m) on average, where n = len(haystack), m = len(needle).
    if needle in haystack:
        # 3. Once we know `needle` occurs, `str.index` gives us the first index.
        #    Also optimized in C, so this call is as fast as it gets in pure Python.
        return haystack.index(needle)

    # 4. If not found, return -1 as specified.
    return -1


# Example usages:
print(strStr('sadbutsad', 'sad'))  # ➞ 0
print(strStr('leetcode', 'leeto'))  # ➞ -1
