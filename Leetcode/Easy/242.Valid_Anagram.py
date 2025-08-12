"""
LEETCODE PROBLEM: 242. Valid Anagram
========================================
Problem Statement:
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word
or phrase, typically using all the original letters exactly once.

Example:
Input: s = "anagram", t = "nagaram"
Output: true

Input: s = "rat", t = "car"
Output: false
"""

# Import Counter from collections module for Method 2
from collections import Counter


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # METHOD 1: SORTING APPROACH
        # ========================================
        # Sorting puts the letters in a defined order, like alphabetical.
        # For example:
        #   sorted("anagram") -> ['a', 'a', 'a', 'g', 'm', 'n', 'r']
        #   sorted("nagaram") -> ['a', 'a', 'a', 'g', 'm', 'n', 'r']
        return sorted(s) == sorted(t)

        # METHOD 2: COUNTER APPROACH
        # ========================================
        # Use Python's Counter to count frequency of each character
        # If both strings have same character frequencies, they're anagrams
        # Time: O(n), Space: O(1) - limited by alphabet size (26 letters)
        return Counter(s) == Counter(t)

        # METHOD 3: MANUAL COUNTING APPROACH
        # ========================================
        """
        METHOD 3 - MANUAL COUNTING:
        1. Check if string lengths are equal (different lengths can't be anagrams)
        2. Create two empty dictionaries to store character counts
        3. Iterate through both strings simultaneously:
            - Count each character's frequency in both strings
            - Use dict.get(key, default) to handle missing keys safely
        4. Compare character counts between dictionaries:
            - If any character has different counts, return False
            - If all characters have matching counts, return True
        """

        # First check: if lengths are different, can't be anagrams
        if len(s) != len(t):
            return False

        # Create dictionaries to store character counts
        countS, countT = {}, {}

        # Count frequency of each character in both strings
        for i in range(len(s)):
            # For string s: get current count (default 0) and add 1
            countS[s[i]] = 1 + countS.get(s[i], 0)
            # For string t: get current count (default 0) and add 1
            countT[t[i]] = 1 + countT.get(t[i], 0)

        # Compare character counts between both dictionaries
        for c in countS:
            # If count doesn't match, not an anagram
            if countS[c] != countT.get(c, 0):
                return False

        # If we reach here, all counts match - it's an anagram
        return True



"""
ALGORITHM EXPLANATION:
================================================================
Steps:

METHOD 1 - SORTING:
1. Sort both input strings character by character
2. Compare the sorted strings for equality
3. If equal, they contain same characters = anagram

METHOD 2 - COUNTER:
1. Use Python's Counter to count character frequencies
2. Compare the two Counter objects for equality
3. Equal counters mean same character frequencies = anagram

METHOD 3 - MANUAL COUNTING:
1. Check if string lengths are equal (different lengths can't be anagrams)
2. Create two empty dictionaries to store character counts
3. Iterate through both strings simultaneously:
   - Count each character's frequency in both strings
   - Use dict.get(key, default) to handle missing keys safely
4. Compare character counts between dictionaries:
   - If any character has different counts, return False
   - If all characters have matching counts, return True

Key Concepts Explained:
- dict.get(key, default): Returns value for key, or default if key doesn't exist
- sorted(): Returns new sorted list of characters
- Counter(): Dictionary subclass that counts hashable objects
"""