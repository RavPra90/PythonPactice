"""
LEETCODE PROBLEM: 27. Remove Element
========================================
Problem Statement:
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
- Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
- The remaining elements of nums are not important as well as the size of nums.
- Return k.

Example:
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
"""

# Approach to solve the problem: Two-Pointer Technique
"""
ALGORITHM EXPLANATION:
================================================================
Steps:
1. Use two pointers: 'i' (slow pointer) and 'j' (fast pointer)
2. The slow pointer 'i' keeps track of the position where the next valid element should be placed
3. The fast pointer 'j' scans through the entire array
4. When we find an element that is NOT equal to 'val', we place it at position 'i' and increment 'i'
5. When we find an element equal to 'val', we skip it (only increment 'j')
6. At the end, 'i' represents the count of valid elements

Time Complexity: O(n) - we traverse the array once
Space Complexity: O(1) - we only use constant extra space

Learning:
- Two-pointer technique is very useful for in-place array modifications
- Slow and fast pointer pattern helps separate valid and invalid elements
- This approach avoids the need for extra space to store results
- The technique can be applied to many similar array filtering problems
- Understanding that we don't need to worry about elements beyond the valid count
"""


def removeElement(nums, val):
    """
    Remove all occurrences of val from nums in-place and return the count of remaining elements.

    Args:
        nums: List[int] - The input array to modify
        val: int - The value to remove from the array

    Returns:
        int - The number of elements in nums which are not equal to val
    """

    # Initialize slow pointer - this will track where to place the next valid element
    i = 0

    # Fast pointer 'j' will scan through the entire array
    # We use range(len(nums)) instead of a separate j variable for clarity
    for j in range(len(nums)):

        # If current element is NOT the value we want to remove
        if nums[j] != val:
            # Place the valid element at position 'i' (slow pointer)
            nums[i] = nums[j]

            # Move slow pointer forward to next position
            i += 1

        # If nums[j] == val, we simply skip it (don't increment i)
        # This effectively "removes" the element by not copying it forward

    # 'i' now represents the count of elements that are not equal to val
    # The first 'i' elements of nums contain all the valid elements
    return i