"""
LEETCODE PROBLEM: 26. Remove Duplicates from Sorted Array
========================================
Problem Statement:
Given an integer array nums sorted in non-decreasing order, remove the duplicates
in-place such that each unique element appears only once. The relative order of
the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
- Change the array nums such that the first k elements of nums contain the unique elements
  in the order they were present in nums initially.
- Return k.

Example:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
"""

# Approach to solve the problem
"""
    ALGORITHM EXPLANATION:
    ================================================================
    Steps:
    1. Use two pointers: 'left' for tracking unique elements position, 'right' for scanning
    2. Start both pointers at beginning, then move 'right' to scan each element
    3. When we find a new unique element (nums[right] != nums[left]), we:
       - Move 'left' pointer forward to next position
       - Copy the unique element to that position
    4. Continue until we've scanned all elements
    5. Return the count of unique elements (left + 1)

    Learning: 
    - Two-pointer technique for in-place array modification
    - Taking advantage of sorted array properties
    - Space-efficient solution with O(1) extra space
    - Understanding in-place algorithms vs creating new arrays
    """


def removeDuplicates(nums):

    # Edge case: if array is empty, return 0
    if not nums:
        return 0

    # Initialize left pointer at index 0
    # This will track the position where we place unique elements
    left = 0

    # Start right pointer from index 1 to compare with previous element
    # Right pointer scans through the entire array
    for right in range(1, len(nums)):

        # If current element is different from the element at left pointer
        # This means we found a new unique element
        if nums[right] != nums[left]:
            # Move left pointer to next position
            # This is where we'll place the new unique element
            left += 1

            # Copy the unique element to the left pointer position
            # This maintains the order of unique elements
            nums[left] = nums[right]

    # Return the count of unique elements
    # Since left is 0-indexed, we add 1 to get the actual count
    return left + 1
