"""
LEETCODE PROBLEM: 13. Roman to Integer
========================================
Problem Statement:
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together.
12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However,
the numeral for four is not IIII. Instead, the number four is written as IV.
Because the one is before the five we subtract it making four. The same principle
applies to the number nine, which is written as IX. There are six instances of this rule:

- I can be placed before V (5) and X (10) to make 4 and 9.
- X can be placed before L (50) and C (100) to make 40 and 90.
- C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

Example:
Input: s = "III"
Output: 3
Explanation: III = 3.

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Input: s = "MCMXC"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90.
"""

# Approach to solve the problem

"""
   ALGORITHM EXPLANATION:
   ================================================================
   Steps:
   1. Create a dictionary mapping each Roman numeral to its integer value
   2. Initialize result to 0
   3. Iterate through the string from left to right
   4. For each character, check if the current character's value is less than 
      the next character's value
   5. If yes, subtract current value (subtraction case like IV, IX, etc.)
   6. If no, add current value (normal case)
   7. Return the final result

   Key Insight: In Roman numerals, when a smaller numeral appears before a 
   larger one, we subtract it. Otherwise, we add it.

   Learning: 
   - Dictionary lookups for mapping values (O(1) time complexity)
   - String traversal with lookahead (checking next character)
   - Pattern recognition in problems (subtraction vs addition cases)
   - Edge case handling (checking bounds before accessing next element)
   """


def romanToInt(s):

    # Step 1: Create a mapping of Roman numerals to their integer values
    # This dictionary allows us to quickly look up the value of any Roman numeral
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    # Step 2: Initialize our result variable to store the final integer
    result = 0

    # Step 3: Iterate through each character in the Roman numeral string
    # We use range(len(s)) so we can access both current and next characters
    for i in range(len(s)):
        # Get the integer value of current Roman numeral character
        current_value = roman_map[s[i]]

        # Step 4: Check if we're not at the last character AND
        # if current value is less than next value
        # This handles subtraction cases like IV (4), IX (9), XL (40), etc.
        if i < len(s) - 1 and current_value < roman_map[s[i + 1]]:
            # Step 5: Subtraction case - subtract current value from result
            # Example: In "IV", when we see 'I' (1) and next is 'V' (5)
            # Since 1 < 5, we subtract 1 from result
            result -= current_value
            print(f"Subtracting {s[i]} ({current_value}) -> Result: {result}")
        else:
            # Step 6: Addition case - add current value to result
            # This is the normal case where we just add the value
            result += current_value
            print(f"Adding {s[i]} ({current_value}) -> Result: {result}")

    # Step 7: Return the final converted integer
    return result