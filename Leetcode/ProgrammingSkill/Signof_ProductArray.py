"""
Implement a function signFunc(x) that returns:

1 if x is positive.
-1 if x is negative.
0 if x is equal to 0.
You are given an integer array nums. Let product be the product of all values in the array nums.
Return signFunc(product).

Example 1:
Input: nums = [-1,-2,-3,-4,3,2,1]
Output: 1
Explanation: The product of all values in the array is 144, and signFunc(144) = 1

Example 2:
Input: nums = [1,5,0,2,-3]
Output: 0
Explanation: The product of all values in the array is 0, and signFunc(0) = 0

Example 3:
Input: nums = [-1,1,-1,1,-1]
Output: -1
Explanation: The product of all values in the array is -1, and signFunc(-1) = -1

"""

def sign (nums):
    if 0 in nums:
        return 0

    mult = 1
    for i in nums:
        mult = mult*i

    if mult < 0:
        return -1
    else:
        return 1

print(sign([-1,-2,-3,-4,3,2,1]))
print(sign([1,5,0,2,-3]))
print(sign([-1,1,-1,1,-1]))

"""
================================================================================================
=============================================================================================
"""

def arraySign(nums):
    """
    Determine the sign of the product of all elements in the array 'nums'.

    Approach:
    1. Check for any zero in the array. If found, return 0 immediately.
    2. Count the number of negative numbers.
    3. If the count of negative numbers is even, return 1 (positive product).
       If odd, return -1 (negative product).

    Examples:
    - Example 1: nums = [-1,-2,-3,-4,3,2,1] → No zeros, 4 negatives (even) → return 1.
    - Example 2: nums = [1,5,0,2,-3] → Zero found → return 0.
    - Example 3: nums = [-1,1,-1,1,-1] → No zeros, 3 negatives (odd) → return -1.
    """
    negative_count = 0  # Initialize counter for negative numbers

    for num in nums:
        if num == 0:
            # If any element is zero, product is zero → return 0
            return 0
        elif num < 0:
            # Increment count for each negative number
            negative_count += 1

    # Determine sign based on even or odd count of negatives
    return 1 if negative_count % 2 == 0 else -1

"""
After processing all elements, the function checks if the count of negative numbers is even or odd. 
An even count results in a positive product (return 1), 
while an odd count results in a negative product (return -1).
"""
print(arraySign([-1,-2,-3,-4,3,2,1]))
print(arraySign([1,5,0,2,-3]))
print(arraySign([-1,1,-1,1,-1]))
