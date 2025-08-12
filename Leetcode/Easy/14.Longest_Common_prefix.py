"""
LEETCODE PROBLEM: 14. Longest Common Prefix
========================================
Problem Statement:
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

# Approach 1: Vertical Scanning (Character by Character)
"""
ALGORITHM EXPLANATION:
================================================================
Steps:
1. Handle edge cases: if array is empty, return ""
2. Start with first character of first string as potential prefix
3. For each character position:
   - Check if all strings have this character at this position
   - Check if the character is the same across all strings
   - If yes, continue to next position
   - If no, return the prefix found so far
4. Return the complete prefix found

Time Complexity: O(S) where S is sum of all characters in all strings
Space Complexity: O(1) - only using a few variables

Learning:
- Vertical scanning technique: comparing characters at same positions across strings
- Early termination when mismatch is found
- Handle edge cases first (empty array, empty strings)
- String slicing and indexing in Python
"""


def longestCommonPrefix(strs):
    """
    Find the longest common prefix among array of strings using vertical scanning.

    Args:
        strs: List of strings
    Returns:
        String: Longest common prefix
    """
    # Edge case: if array is empty, return empty string
    if not strs:
        return ""

    # Edge case: if array has only one string, return that string
    if len(strs) == 1:
        return strs[0]

    # Start checking character by character from position 0
    for i in range(len(strs[0])):  # Use first string's length as reference
        # Get the character at position i from first string
        current_char = strs[0][i]

        # Check this character against all other strings
        for j in range(1, len(strs)):  # Start from second string (index 1)
            # Check two conditions:
            # 1. Does current string have character at position i?
            # 2. Is the character same as first string's character?
            if i >= len(strs[j]) or strs[j][i] != current_char:
                # If either condition fails, return prefix found so far
                return strs[0][:i]  # Return substring from start to position i

    # If we reach here, entire first string is common prefix
    return strs[0]


# Approach 2: Horizontal Scanning (String by String)
"""
ALGORITHM EXPLANATION:
================================================================
Steps:
1. Start with first string as initial prefix
2. Compare this prefix with each subsequent string
3. For each string, find common prefix between current prefix and this string
4. Update the prefix to this common part
5. If at any point prefix becomes empty, return ""
6. Return final prefix

Learning:
- Horizontal scanning: comparing prefix with one string at a time
- Reducing the problem step by step
- Using helper function to find common prefix between two strings
"""


def longestCommonPrefix_v2(strs):
    """
    Find longest common prefix using horizontal scanning approach.
    """
    if not strs:
        return ""

    # Start with first string as initial prefix
    prefix = strs[0]

    # Compare with each subsequent string
    for i in range(1, len(strs)):
        # Find common prefix between current prefix and current string
        prefix = getCommonPrefix(prefix, strs[i])
        # Early termination: if no common prefix, return immediately
        if not prefix:
            return ""

    return prefix


def getCommonPrefix(str1, str2):
    """
    Helper function to find common prefix between two strings.
    """
    min_length = min(len(str1), len(str2))  # Compare up to shorter string's length

    for i in range(min_length):
        if str1[i] != str2[i]:
            return str1[:i]  # Return common part found so far

    # If we reach here, one string is prefix of another
    return str1[:min_length]


# Approach 3: Using Built-in Functions (Pythonic Way)
"""
ALGORITHM EXPLANATION:
================================================================
Steps:
1. Use zip() to group characters at same positions from all strings
2. Use set() to check if all characters at each position are same
3. Use itertools.takewhile() to take characters while they're all same
4. Join the result to form the prefix

Learning:
- Using Python's built-in functions for elegant solutions
- zip() function for parallel iteration
- set() for uniqueness checking
- Generator expressions and functional programming concepts
"""

from itertools import takewhile


def longestCommonPrefix_v3(strs):
    """
    Pythonic solution using zip and takewhile.
    """
    if not strs:
        return ""

    # zip(*strs) groups characters at same positions
    # takewhile continues while condition is true
    # len(set(chars)) == 1 means all characters are same
    return ''.join(char for char, in takewhile(lambda x: len(set(x)) == 1, zip(*strs)))


# Approach 4: Min-Max String Comparison (Your Suggested Approach)
"""
ALGORITHM EXPLANATION:
================================================================
🧠 THE BRILLIANT INSIGHT:
If we arrange all strings in lexicographical (dictionary) order, the first 
and last strings represent the "extremes". If these extreme strings share 
a common prefix, then ALL strings in between MUST also share that prefix!

Example: ["flower", "flow", "flight"]
- Lexicographical order: "flight" < "flow" < "flower"  
- Min string: "flight"
- Max string: "flower"
- If "flight" and "flower" share prefix "fl", then "flow" must too!

WHY THIS WORKS:
Think of dictionary ordering - if two words at opposite ends of the dictionary 
share the same starting letters, then every word between them MUST start 
with those same letters!

Steps:
1. Find lexicographically smallest string (min_str) using min()
2. Find lexicographically largest string (max_str) using max()  
3. Compare characters of min_str and max_str position by position
4. If characters match, continue to next position
5. If characters don't match, return the prefix found so far
6. If we finish the loop, entire min_str is the common prefix

Time Complexity: O(n + m) where n = total chars to find min/max, m = length of min_str
Space Complexity: O(1) extra space (not counting result string)

Learning:
- Lexicographical ordering properties and how to exploit them
- Using min/max functions creatively on strings
- Mathematical insight: comparing extremes to deduce properties of the whole set
- Reducing a multi-string problem to a two-string problem
"""


def longestCommonPrefix_minmax(strs):
    """
    Find longest common prefix using min-max string comparison.
    This is your brilliant approach! Let's trace through it step by step.
    """
    # Edge case: empty array
    if not strs:
        return ""

    # STEP 1: Find the lexicographical extremes
    # min() finds the string that comes first in dictionary order
    # max() finds the string that comes last in dictionary order

    # Example with ["flower", "flow", "flight"]:
    # - "flight" comes first alphabetically (f-l-i...)
    # - "flower" comes last alphabetically (f-l-o...)

    min_str = min(strs)  # This will be "flight"
    max_str = max(strs)  # This will be "flower"

    print(f"🔍 Min string (lexicographically first): '{min_str}'")
    print(f"🔍 Max string (lexicographically last): '{max_str}'")

    # STEP 2: Compare character by character
    result = ""

    # We only need to check up to the length of the shorter string
    # (which will be min_str in most cases)
    for i in range(len(min_str)):
        # If characters at position i are the same in both extremes
        if min_str[i] == max_str[i]:
            result += min_str[i]  # Add this character to our prefix
        else:
            # First mismatch found - no need to check further
            return result

    # If we reach here, entire min_str is a prefix of max_str
    return result


# OPTIMIZED VERSION (Your code with efficiency improvement)
def longestCommonPrefix_your_optimized(strs):
    """
    Your approach but optimized to avoid string concatenation in loop.
    This is the version you should use in interviews!
    """
    if not strs:
        return ""

    # Get lexicographical extremes - same as before
    min_str = min(strs)
    max_str = max(strs)

    # Find the first position where characters differ
    for i in range(len(min_str)):
        if min_str[i] != max_str[i]:
            # Return everything up to (but not including) position i
            return min_str[:i]

    # If no mismatch found, entire min_str is the prefix
    return min_str
