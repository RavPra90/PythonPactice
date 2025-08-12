"""
LEETCODE PROBLEM: 1. Two Sum
========================================
Problem Statement:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 2 + 7 == 9, we return [0, 1].

Input: nums = [3,2,4], target = 6
Output: [1,2]

Input: nums = [3,3], target = 6
Output: [0,1]
"""

# Approach 1: Brute Force (Less Efficient)
"""
ALGORITHM EXPLANATION - BRUTE FORCE:
================================================================
Steps:
1. Use two nested loops to check every pair of numbers
2. For each number at index i, check all numbers after it (index j where j > i)
3. If nums[i] + nums[j] equals target, return [i, j]
4. Continue until we find the pair

Time Complexity: O(n²) - we check every pair
Space Complexity: O(1) - only using a few variables

Learning: This approach works but is slow for large arrays because we're doing redundant work.
"""


def twoSum_bruteforce(nums, target):
    # Loop through each element in the array
    for i in range(len(nums)):
        # For each element, check all elements that come after it
        for j in range(i + 1, len(nums)):
            # If the sum of current pair equals target, we found our answer
            if nums[i] + nums[j] == target:
                return [i, j]

    # This line should never be reached based on problem constraints
    return []


# Approach 2: Hash Map (More Efficient) - RECOMMENDED SOLUTION
"""
ALGORITHM EXPLANATION - HASH MAP:
================================================================
Steps:
1. Create an empty hash map (dictionary) to store numbers we've seen
2. For each number in the array:
   a. Calculate what number we need to reach our target (complement = target - current_number)
   b. Check if this complement exists in our hash map
   c. If yes, return the indices [complement_index, current_index]
   d. If no, store the current number and its index in hash map for future use
3. Continue until we find the pair

Time Complexity: O(n) - we only go through the array once
Space Complexity: O(n) - we might store up to n elements in our hash map

Learning: Hash maps allow us to trade space for time - we use more memory but solve the problem much faster!
"""


def twoSum(nums, target):
    # Create a dictionary to store number -> index mapping
    # Key: the number we've seen i.e. value , Value: its index in the array
    seen = {}

    # Loop through each number with its index
    for i, num in enumerate(nums):
        # Calculate what number we need to add to current number to get target
        diff = target - num

        # Check if we've already seen this complement number
        if diff in seen:
            # Found it! Return the index where we saw the complement and current index
            return [seen[diff], i]

        # Haven't found the pair yet, so store current number and its index
        # for future reference
        seen[num] = i

    # This should never be reached based on problem constraints
    return []