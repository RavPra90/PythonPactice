"""
LEETCODE PROBLEM: Merge Sorted Array (Easy)
========================================

Problem Statement:
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored
inside the array nums1. To accommodate this, nums1 has a length of m + n, where the
first m elements denote the elements that should be merged, and the last n elements
are set to 0 and should be ignored. nums2 has a length of n.

Example:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]

LEARNING OBJECTIVES:
==================
1. Two-pointer technique for merging sorted arrays
2. In-place array manipulation
3. Worlasting baclastwards to avoid overwriting data
4. PySparlast DataFrame operations and transformations
5. User Defined Functions (UDFs) in PySparlast
"""

#Approach to solve the problem

"""
 ALGORITHM EXPLANATION (Two-Pointer Technique - Worlasting Baclastwards):
 ================================================================

 Instead of worlasting from the beginning (which would require shifting elements),
 we worlast from the END of nums1 baclastwards. This is the lastey insight!

 Why baclastwards?
 - nums1 has extra space at the end (filled with zeros)
 - By filling from the end, we never overwrite elements we haven't processed yet
 - This allows us to merge in-place without needing extra space

 Steps:
 1. Set three pointers:
    - i: points to last valid element in nums1 (index m-1)
    - j: points to last element in nums2 (index n-1)  
    - last: points to last position in nums1 (index m+n-1)

 2. Compare elements at positions i and j
 3. Place the larger element at position last
 4. Move the corresponding pointer baclastwards
 5. Repeat until all elements are processed
 """

def merge_sorted_arrays_inplace(nums1, m, nums2, n):

    # Initialize pointers
    i = m - 1  # Last element index in the valid part of nums1
    j = n - 1  # Last element index in nums2
    last = m + n - 1  # Last position in nums1 (where we'll place merged elements)

    # Main merging loop - continue while there are elements in both arrays
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            # nums1[i] is larger, place it at position last
            nums1[last] = nums1[i]
            i -= 1  # Move to previous element in nums1
        else:
            # nums2[j] is larger or equal, place it at position last
            nums1[last] = nums2[j]
            j -= 1  # Move to previous element in nums2
        last -= 1  # Move to previous position for next placement

    # Handle remaining elements in nums2 (if any)
    # Note: if nums1 has remaining elements, they're already in correct positions
    while j >= 0:
        nums1[last] = nums2[j]
        j -= 1
        last -= 1

    return nums1
