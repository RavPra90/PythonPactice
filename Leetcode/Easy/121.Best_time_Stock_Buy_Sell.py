"""
LEETCODE PROBLEM: 121. Best Time to Buy and Sell Stock
========================================
Problem Statement:
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one share of stock
and choosing a different day in the future to sell that share.

Return the maximum profit you can achieve from this transaction. If you cannot achieve
any profit, return 0.

Example:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

Input: prices = [7,6,4,3,2,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""


# Two-Pointer Approach to solve the problem
def maxProfit(prices):
    """
    ALGORITHM EXPLANATION:
    ================================================================
    Steps:
    1. Initialize two pointers: left (buy day) at index 0, right (sell day) at index 1
    2. Initialize maxP to track maximum profit (starts at 0)
    3. While right pointer is within array bounds:
       a. If prices[left] < prices[right]: We can profit, calculate and update maxP
       b. If prices[left] >= prices[right]: Found better buy price, move left to right
       c. Always increment right pointer to explore next selling day
    4. Return maximum profit found

    Key Insight: This uses a sliding window/two-pointer technique where:
    - Left pointer always points to the best buying opportunity seen so far
    - Right pointer explores all possible selling days after the buy day
    - When we find a lower price than current buy price, we update buy position

    Learning:
    - Two-pointer technique for optimization problems
    - Greedy approach: always maintain the best buying position
    - Single-pass algorithm achieving O(n) time complexity
    - Understanding when to move pointers in two-pointer problems
    - Sliding window pattern with dynamic left boundary
    """

    # Edge case: need at least 2 prices to make a transaction
    if len(prices) < 2:
        return 0

    # Step 1: Initialize pointers and maximum profit tracker
    # l: left pointer (buy day), starts at day 0
    # r: right pointer (sell day), starts at day 1
    # maxP: maximum profit achievable, initially 0
    l, r = 0, 1
    maxP = 0

    # Step 2: Iterate through array with right pointer
    while r < len(prices):

        # Step 3: Check if current left-right pair can generate profit
        if prices[l] < prices[r]:
            # We can make profit! Calculate current profit
            profit = prices[r] - prices[l]
            # Update maximum profit if current profit is better
            maxP = max(maxP, profit)
        else:
            # Current left position is not optimal for buying
            # We found a better (lower) price at position r
            # Move left pointer to this better buying opportunity
            l = r

        # Step 4: Always move right pointer to explore next selling day
        r += 1

    # Step 5: Return the maximum profit found
    return maxP


# Alternative implementation showing the equivalence with min-price tracking
def maxProfitMinTracking(prices):
    """
    Traditional approach for comparison - tracks minimum price seen so far
    This is mathematically equivalent to the two-pointer approach above
    """
    if len(prices) < 2:
        return 0

    # Track the minimum price encountered (best buying price)
    min_price = prices[0]
    max_profit = 0

    # Iterate through remaining prices
    for i in range(1, len(prices)):
        current_price = prices[i]

        # Update minimum price if we find a lower one
        if current_price < min_price:
            min_price = current_price

        # Calculate profit if we sell at current price
        profit = current_price - min_price
        # Update maximum profit
        max_profit = max(max_profit, profit)

    return max_profit