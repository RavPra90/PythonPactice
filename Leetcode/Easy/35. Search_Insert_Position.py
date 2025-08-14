"""
LEETCODE PROBLEM: 35. Search Insert Position
========================================
Problem Statement:
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example:
Input: nums = [1,3,5,6], target = 5
Output: 2

Input: nums = [1,3,5,6], target = 2
Output: 1

Input: nums = [1,3,5,6], target = 7
Output: 4
"""

# Approach to solve the problem
"""
ALGORITHM EXPLANATION:
================================================================
Steps:
1. Use Binary Search since the array is sorted and we need O(log n) complexity
2. Initialize two pointers: left = 0, right = length of array - 1
3. While left <= right:
   - Calculate middle index
   - If middle element equals target, return middle index
   - If middle element is less than target, search in right half (left = mid + 1)
   - If middle element is greater than target, search in left half (right = mid - 1)
4. If target is not found, left pointer will be at the correct insertion position

Learning:
- Binary Search is perfect for sorted arrays with O(log n) time complexity
- When target is not found, the left pointer naturally points to the insertion position
- This happens because when we exit the loop, left > right, and left is where target should be inserted
- Understanding pointer positions after binary search helps solve many insertion problems
"""


def searchInsert(nums, target):
    """
    Find the index of target in sorted array, or return insertion position if not found.

    Args:
        nums: List of integers in sorted order
        target: Integer to search for

    Returns:
        Integer representing index of target or insertion position
    """

    # Initialize left and right pointers for binary search
    left = 0
    right = len(nums) - 1

    # Continue searching while search space is valid
    while left <= right:
        # Calculate middle index to avoid overflow
        # Using (left + right) // 2 works for Python, but (left + (right - left) // 2) is safer in other languages
        mid = (left + right) // 2

        # Case 1: Found the target at middle position
        if nums[mid] == target:
            return mid

        # Case 2: Middle element is smaller than target
        # Target must be in the right half, so move left pointer
        elif nums[mid] < target:
            left = mid + 1

        # Case 3: Middle element is greater than target
        # Target must be in the left half, so move right pointer
        else:
            right = mid - 1

    # If we exit the loop, target was not found
    # At this point, left > right, and left is the correct insertion position
    # This is because:
    # - All elements to the left of 'left' are < target
    # - All elements to the right of 'left' are > target
    return left


"""
DETAILED WALKTHROUGH EXAMPLE:
========================================
Let's trace through: nums = [1, 3, 5, 6], target = 2

INITIAL STATE:
Array:  [1, 3, 5, 6]
Index:   0  1  2  3
left = 0, right = 3, target = 2

ITERATION 1:
- left (0) <= right (3)? YES, continue
- mid = (0 + 3) // 2 = 1
- nums[mid] = nums[1] = 3
- Compare: 3 vs 2
- nums[mid] (3) > target (2), so target is in LEFT half
- Update: right = mid - 1 = 0
- New state: left = 0, right = 0

ITERATION 2:
- left (0) <= right (0)? YES, continue
- mid = (0 + 0) // 2 = 0
- nums[mid] = nums[0] = 1
- Compare: 1 vs 2
- nums[mid] (1) < target (2), so target is in RIGHT half
- Update: left = mid + 1 = 1
- New state: left = 1, right = 0

LOOP EXIT:
- left (1) <= right (0)? NO, exit loop
- Return left = 1

RESULT: Target 2 should be inserted at index 1
Final array would be: [1, 2, 3, 5, 6]
                      0  1  2  3  4

========================================
Another Example: nums = [1, 3, 5, 6], target = 5

INITIAL STATE:
left = 0, right = 3, target = 5

ITERATION 1:
- mid = (0 + 3) // 2 = 1
- nums[1] = 3
- 3 < 5, so go RIGHT
- left = 2, right = 3

ITERATION 2:
- mid = (2 + 3) // 2 = 2
- nums[2] = 5
- 5 == 5, FOUND!
- Return 2

========================================
Edge Case: nums = [1, 3, 5, 6], target = 7

INITIAL STATE:
left = 0, right = 3, target = 7

ITERATION 1:
- mid = 1, nums[1] = 3
- 3 < 7, go RIGHT
- left = 2, right = 3

ITERATION 2:
- mid = 2, nums[2] = 5
- 5 < 7, go RIGHT
- left = 3, right = 3

ITERATION 3:
- mid = 3, nums[3] = 6
- 6 < 7, go RIGHT
- left = 4, right = 3

LOOP EXIT:
- left (4) > right (3), exit
- Return left = 4 (insert at end)
"""

# Alternative Linear Search Approach (Your Code)
"""
ANALYSIS OF LINEAR SEARCH APPROACH:
================================================================
Your code: def searchInsert(nums, target):
    for i in range(len(nums)):
        if nums[i] != target:
            if target < nums[i]:
                return i
        else:
            return i
    return i+1

CORRECTNESS: ✅ Yes, this code is CORRECT and will produce right results
EFFICIENCY: ❌ O(n) time complexity - does NOT meet LeetCode's O(log n) requirement

How it works:
1. Iterate through each element in the array
2. If current element equals target, return current index
3. If current element is greater than target, return current index (insertion point)
4. If we finish the loop without returning, target goes at the end (i+1)

Why it's correct but not optimal:
- It correctly handles all test cases and edge cases
- However, it doesn't utilize the fact that the array is SORTED
- Linear search takes O(n) time, but the problem specifically asks for O(log n)
- For large arrays, this will be much slower than binary search
"""


def searchInsert_Linear(nums, target):
    """
    Linear search approach - correct but not meeting time complexity requirement
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    for i in range(len(nums)):
        if nums[i] != target:
            if target < nums[i]:
                return i
        else:
            return i
    return i + 1


# Test cases comparing both approaches
if __name__ == "__main__":
    test_cases = [
        ([1, 3, 5, 6], 5, 2),  # Target found
        ([1, 3, 5, 6], 2, 1),  # Insert in middle
        ([1, 3, 5, 6], 7, 4),  # Insert at end
        ([1, 3, 5, 6], 0, 0),  # Insert at beginning
    ]

    for nums, target, expected in test_cases:
        binary_result = searchInsert(nums, target)
        linear_result = searchInsert_Linear(nums, target)

        # Both should give same results
        assert binary_result == linear_result == expected