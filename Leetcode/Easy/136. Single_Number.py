"""
LEETCODE PROBLEM: 136. Single Number
========================================
Problem Statement:
Given a non-empty array of integers nums, every element appears twice except for one.
Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example:
Input: nums = [2,2,1]
Output: 1

Input: nums = [4,1,2,1,2]
Output: 4

Input: nums = [1]
Output: 1
"""


# Approach to solve the problem using XOR bitwise operation
def singleNumber(nums):
    """
    Find the single number that appears only once in an array where all other numbers appear twice.

    Args:
        nums: List of integers where every element appears twice except one

    Returns:
        The single number that appears only once
    """

    # Initialize result to 0
    # We'll use XOR operation to find the unique number
    result = 0

    # Iterate through each number in the array
    for num in nums:
        # XOR the current number with result
        # Key insight: XOR of two same numbers is 0, XOR of any number with 0 is the number itself
        result ^= num

    # After XORing all numbers, only the unique number will remain
    return result


"""
ALGORITHM EXPLANATION:
================================================================
Steps:
1. Initialize a variable 'result' to 0
2. Iterate through each number in the input array
3. Perform XOR operation between 'result' and current number
4. After processing all numbers, 'result' will contain the single number

How XOR works in this context:
- XOR (^) is a bitwise operation
- Key properties of XOR:
  * a ^ a = 0 (any number XORed with itself equals 0)
  * a ^ 0 = a (any number XORed with 0 equals the number itself)
  * XOR is commutative: a ^ b = b ^ a
  * XOR is associative: (a ^ b) ^ c = a ^ (b ^ c)

Example walkthrough with [4,1,2,1,2]:
- result = 0
- result = 0 ^ 4 = 4
- result = 4 ^ 1 = 5 (in binary: 100 ^ 001 = 101)
- result = 5 ^ 2 = 7 (in binary: 101 ^ 010 = 111)
- result = 7 ^ 1 = 6 (in binary: 111 ^ 001 = 110)
- result = 6 ^ 2 = 4 (in binary: 110 ^ 010 = 100)
- Final result: 4

Why this works:
Since every number except one appears twice, when we XOR all numbers:
- Each pair of identical numbers will cancel out to 0
- Only the single number will remain

Time Complexity: O(n) - we visit each element once
Space Complexity: O(1) - we only use constant extra space

Learning:
================================================================
1. XOR Operation Mastery:
   - Understanding XOR properties is crucial for many bit manipulation problems
   - XOR can be used to find differences, toggle bits, and solve pairing problems

2. Bit Manipulation Techniques:
   - Bitwise operations are often more efficient than arithmetic operations
   - They can solve complex problems with elegant, space-efficient solutions

3. Mathematical Properties in Programming:
   - Leveraging mathematical properties (like XOR's self-canceling nature) 
     can lead to optimal solutions
   - Sometimes the most efficient solution involves thinking beyond traditional approaches

4. Pattern Recognition:
   - Problems involving pairs/duplicates often have bit manipulation solutions
   - When you see "find the unique element" or "all others appear twice", think XOR

5. Space-Time Trade-offs:
   - This solution achieves O(1) space complexity instead of using a hash set (O(n) space)
   - Understanding when to prioritize space vs time complexity is important

Future Applications:
- Finding missing numbers in sequences
- Detecting differences between two similar datasets
- Encryption and data integrity checks
- State toggling in systems programming
"""