"""
LEETCODE PROBLEM: 70. Climbing Stairs
========================================
Problem Statement:
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

# Approach to solve the problem: Dynamic Programming using Fibonacci Pattern
"""
ALGORITHM EXPLANATION:
================================================================
This problem follows the Fibonacci sequence pattern!

Key Insight: To reach step n, you can come from:
- Step (n-1) by taking 1 step, OR
- Step (n-2) by taking 2 steps

So: ways(n) = ways(n-1) + ways(n-2)

Steps:
1. Start with base cases: 1 way for step 0, 1 way for step 1
2. For each step from 2 to n, add the ways from previous two steps
3. Use two variables (one, two) to track the last two Fibonacci numbers
4. Swap values using a temporary variable to move forward in sequence
5. After n-1 iterations, 'one' will contain our answer

Learning: 
- Fibonacci sequence appears in many climbing/counting problems
- Dynamic Programming optimizes recursive solutions from O(2^n) to O(n)
- Variable swapping technique is crucial for space-efficient solutions
- Pattern: each step depends on sum of previous two steps
- Time: O(n), Space: O(1) - optimal solution!
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        # Handle base case
        if n <= 1:
            return 1

        # Initialize two variables following the reference pattern
        # 'one' represents current Fibonacci number
        # 'two' represents previous Fibonacci number
        one, two = 1, 1

        # We need to iterate (n-1) times to get the nth Fibonacci number
        # This is because we start from F(1) and need to reach F(n)
        for i in range(n - 1):
            # Store current 'one' value temporarily
            temp = one

            # Calculate next Fibonacci number: F(i+1) = F(i) + F(i-1)
            one = one + two  # New 'one' = current + previous

            # Move previous value: what was 'one' becomes new 'two'
            two = temp

            # Alternative one-liner for swapping: one, two = one + two, one

        return one


# Visual explanation of how variables change:
"""
Let's trace through n = 5:

Initial: one = 1, two = 1

Iteration 1 (i=0):
  temp = 1 (store current 'one')
  one = 1 + 1 = 2 (F(2))
  two = 1 (previous 'one')
  Current state: one=2, two=1

Iteration 2 (i=1):
  temp = 2
  one = 2 + 1 = 3 (F(3))
  two = 2
  Current state: one=3, two=2

Iteration 3 (i=2):
  temp = 3
  one = 3 + 2 = 5 (F(4))
  two = 3
  Current state: one=5, two=3

Iteration 4 (i=3):
  temp = 5
  one = 5 + 3 = 8 (F(5))
  two = 5
  Final state: one=8, two=5

Answer: 8 ways to climb 5 stairs
"""


# Alternative cleaner version using tuple unpacking
class SolutionCleaner:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1

        one, two = 1, 1

        for i in range(n - 1):
            # Python allows simultaneous assignment
            # This is equivalent to the temp variable approach
            one, two = one + two, one

        return one