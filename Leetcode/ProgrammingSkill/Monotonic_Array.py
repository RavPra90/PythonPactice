"""
An array is monotonic if it is either monotone increasing or monotone decreasing.
An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].
Given an integer array nums, return true if the given array is monotonic, or false otherwise.

Example 1:
Input: nums = [1,2,2,3]
Output: true

Example 2:
Input: nums = [6,5,4,4]
Output: true

Example 3:
Input: nums = [1,3,2]
Output: false
"""



def is_Monotonic(arr):
    return arr == sorted(arr) or arr == sorted(arr, reverse=True)

print(is_Monotonic([6,5,4,4]))
print(is_Monotonic([1,2,2,3]))
print(is_Monotonic([1,3,2]))

#But for large arrays, this would sort the array twice, which is O(n log n) each time. Hence it is not efficient.

"""
=====================================================================================================
======================================================================================================
"""

#EFFICIENT APPROACH
def is_sorted(arr):
    """
    Checks if an array is sorted in either non-decreasing (ascending) or non-increasing (descending) order.

    Approach:
    1. Check if all adjacent elements are in non-decreasing order (ascending).
    2. Check if all adjacent elements are in non-increasing order (descending).
    3. Return True if either check passes.

    Examples:
    - [1, 2, 3] → Ascending → True
    - [3, 2, 1] → Descending → True
    - [1, 3, 2] → Not sorted → False
    - [2, 2, 2] → Both → True
    - [] → Empty list → True
    """
    # Edge case: empty or single-element lists are considered sorted
    if len(arr) <= 1:
        return True
    """
    all() Function:
    Checks if all elements in an iterable are True.

    Example: all([True, True, False]) → False.
    
    When to Use This Approach
    
    Large Lists: Avoids creating sorted copies (memory-efficient).
    Mixed Orders: Handles both ascending and descending checks in a single pass.
    Duplicates: Works for arrays with repeated values (e.g., [2, 2, 2]).
    """

    # Check for ascending order (non-decreasing)
    """
    Check Ascending Order:
    Use all(arr[i] <= arr[i+1] to verify every element is ≤ the next.
    Example: [1, 2, 3] → True because 1 <= 2 <= 3.
    """
    is_ascending = all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

    # Check for descending order (non-increasing)
    """
    Check Descending Order:
    Use all(arr[i] >= arr[i+1] to verify every element is ≥ the next.
    Example: [5, 3, 1] → True because 5 >= 3 >= 1.
    """
    is_descending = all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1))

    return is_ascending or is_descending

print(is_sorted([6,5,4,4]))
print(is_sorted([1,2,2,3]))
print(is_sorted([1,3,2]))