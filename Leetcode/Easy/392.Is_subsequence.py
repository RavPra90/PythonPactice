"""
LEETCODE PROBLEM: 392. Is Subsequence
========================================
Problem Statement:
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string 
by deleting some (can be none) of the characters without disturbing the relative 
order of the remaining characters.

Example:
Input: s = "abc", t = "aebdgc"
Output: true
Explanation: We can find 'a', 'b', 'c' in t while maintaining their order.

Input: s = "axc", t = "ahbgdc" 
Output: false
Explanation: 'x' is not present in t, so s cannot be a subsequence of t.
"""


# Approach to solve the problem: Two Pointers Technique
def isSubsequence(s, t):
    """
    Check if string s is a subsequence of string t using two pointers.

    Args:
        s (str): The subsequence string to check
        t (str): The main string to search in

    Returns:
        bool: True if s is a subsequence of t, False otherwise
    """
    # Initialize two pointers
    # s_pointer: tracks position in subsequence string s
    # t_pointer: tracks position in main string t
    s_pointer = 0
    t_pointer = 0

    # Continue until we've checked all characters in either string
    while s_pointer < len(s) and t_pointer < len(t):
        # If characters match, move pointer in subsequence string
        if s[s_pointer] == t[t_pointer]:
            s_pointer += 1  # Found a matching character, move to next in s

        # Always move pointer in main string (whether match found or not)
        t_pointer += 1

    # If we've matched all characters in s, then s is a subsequence of t
    # This happens when s_pointer equals the length of s
    return s_pointer == len(s)


"""
ALGORITHM EXPLANATION:
================================================================
Steps:
1. Initialize two pointers: one for string s (subsequence) and one for string t (main string)
2. Iterate through both strings simultaneously:
   - If characters at both pointers match, advance the subsequence pointer
   - Always advance the main string pointer
3. Continue until we reach the end of either string
4. Return True if we've matched all characters in the subsequence (s_pointer == len(s))

Time Complexity: O(n) where n is the length of string t
Space Complexity: O(1) - only using two pointer variables

Learning:
- Two Pointers Technique: Efficient way to traverse two data structures simultaneously
- Greedy Approach: We match characters as soon as we find them (first occurrence)
- String Traversal: Understanding how to iterate through strings with different speeds
- Subsequence vs Substring: Subsequence allows gaps, substring requires consecutive characters
- Early Termination: We can stop as soon as we find all characters or exhaust the main string

Example Walkthrough:
s = "abc", t = "aebdgc"

Initial: s_pointer = 0, t_pointer = 0
Step 1: s[0]='a', t[0]='a' → Match! s_pointer=1, t_pointer=1
Step 2: s[1]='b', t[1]='e' → No match, s_pointer=1, t_pointer=2  
Step 3: s[1]='b', t[2]='b' → Match! s_pointer=2, t_pointer=3
Step 4: s[2]='c', t[3]='d' → No match, s_pointer=2, t_pointer=4
Step 5: s[2]='c', t[4]='g' → No match, s_pointer=2, t_pointer=5
Step 6: s[2]='c', t[5]='c' → Match! s_pointer=3, t_pointer=6

Result: s_pointer (3) == len(s) (3) → Return True
"""


# Test cases to verify the solution
def test_solution():
    # Test case 1: Basic subsequence
    assert isSubsequence("abc", "aebdgc") == True

    # Test case 2: Not a subsequence
    assert isSubsequence("axc", "ahbgdc") == False

    # Test case 3: Empty subsequence (always true)
    assert isSubsequence("", "abc") == True

    # Test case 4: Same strings
    assert isSubsequence("abc", "abc") == True

    # Test case 5: Subsequence longer than main string
    assert isSubsequence("abc", "ab") == False