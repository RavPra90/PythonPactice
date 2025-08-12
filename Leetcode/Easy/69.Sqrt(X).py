"""
LEETCODE PROBLEM: 69. Sqrt(x)
========================================
Problem Statement:
Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) or x ** 0.5.


Example:
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.828..., and since we round it down to the nearest integer, we return 2.
"""

# Approach to solve the problem: Binary Search with Three-Way Comparison
"""
ALGORITHM EXPLANATION:
================================================================
We use binary search to find the exact square root or the largest integer whose square is ≤ x.
The key insight is to use three-way comparison:

1. If mid² > x: Answer is smaller, search left half
2. If mid² < x: Answer could be larger, search right half  
3. If mid² = x: Found exact answer!

Why return 'right' at the end?
- When loop ends, left > right
- 'right' will be the largest value where mid² ≤ x
- 'left' will be the smallest value where mid² > x
- So 'right' is our floor(sqrt(x))

Steps:
1. Set search boundaries: left = 1, right = x
2. Find middle point and calculate mid²
3. Compare mid² with x using three conditions
4. Adjust boundaries based on comparison
5. If exact match found, return immediately
6. If no exact match, return 'right' (largest valid value)

Learning:
- Binary Search with three-way comparison pattern
- Understanding why 'right' gives us the floor value
- Loop invariant: answer is always in range [left, right]
- Classic "find floor value" binary search template
- Always analyze what left/right represent when loop terminates
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        # Handle the edge case for x = 0
        if x == 0:
            return 0

        # Set up binary search boundaries
        left, right = 1, x

        # Binary search for square root
        while left <= right:
            # Calculate middle point
            mid = (left + right) // 2

            # Three-way comparison with x
            if mid * mid > x:
                # mid is too large, search in smaller values
                # Answer must be in [left, mid-1]
                right = mid - 1

            elif mid * mid < x:
                # mid is too small, search in larger values
                # Answer must be in [mid+1, right]
                left = mid + 1

            else:
                # Perfect match! mid² = x
                return mid

        # When we exit the loop: left > right
        # 'right' is the largest integer where right² ≤ x
        # 'left' is the smallest integer where left² > x
        # Therefore, 'right' is our answer (floor of square root)
        return right


# Let's trace through examples to understand why we return 'right'
"""
Example 1: x = 8 (perfect square doesn't exist, expect 2)

Initial: left=1, right=8

Iteration 1:
  mid = (1+8)//2 = 4
  mid² = 16 > 8, so right = mid-1 = 3
  New range: left=1, right=3

Iteration 2:
  mid = (1+3)//2 = 2  
  mid² = 4 < 8, so left = mid+1 = 3
  New range: left=3, right=3

Iteration 3:
  mid = (3+3)//2 = 3
  mid² = 9 > 8, so right = mid-1 = 2
  New range: left=3, right=2

Now left > right, loop ends
Return right = 2 ✓

Example 2: x = 9 (perfect square exists, expect 3)

Initial: left=1, right=9

Iteration 1:
  mid = (1+9)//2 = 5
  mid² = 25 > 9, so right = mid-1 = 4
  New range: left=1, right=4

Iteration 2:
  mid = (1+4)//2 = 2
  mid² = 4 < 9, so left = mid+1 = 3
  New range: left=3, right=4

Iteration 3:
  mid = (3+4)//2 = 3
  mid² = 9 = 9, return mid = 3 ✓
"""
