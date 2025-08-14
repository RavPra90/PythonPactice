"""
LEETCODE PROBLEM: 66. Plus One
========================================
Problem Statement:
You are given a large integer represented as an integer array digits, where each
digits[i] is the ith digit of the integer. The digits are ordered from most significant
to least significant in left-to-right order. The large integer does not contain any leading zeros.

Increment the large integer by one and return the resulting array of digits.

Example:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123. Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321. Incrementing by one gives 4321 + 1 = 4322.

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9. Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
"""


# Approach 1: Simple and Intuitive Approach
def plusOne_simple(digits):
    """
    This approach handles the addition from right to left, managing carries properly.
    Time Complexity: O(n) where n is the length of digits array
    Space Complexity: O(1) if we don't count the output array, O(n) if we do
    """
    # Start from the rightmost digit (least significant digit)
    # We iterate backwards through the array
    for i in range(len(digits) - 1, -1, -1):

        # If current digit is less than 9, we can simply add 1 and return
        if digits[i] < 9:
            digits[i] += 1
            return digits

        # If current digit is 9, it becomes 0 after adding 1 (carry over)
        # We need to continue to the next digit (going left)
        digits[i] = 0

    # If we reach here, it means all digits were 9
    # Example: [9,9,9] becomes [1,0,0,0]
    # We need to create a new array with one extra digit
    return [1] + digits


# Approach 2: More Explicit Carry Handling
def plusOne_with_carry(digits):
    """
    This approach explicitly tracks the carry value, making the logic clearer.
    Time Complexity: O(n) where n is the length of digits array
    Space Complexity: O(1) if we don't count the output array
    """
    # Initialize carry to 1 (since we're adding 1 to the number)
    carry = 1

    # Process digits from right to left (least to most significant)
    for i in range(len(digits) - 1, -1, -1):
        # Add carry to current digit
        total = digits[i] + carry

        # Update current digit (total % 10 gives us the digit to store)
        digits[i] = total % 10

        # Calculate new carry (total // 10 gives us the carry for next iteration)
        carry = total // 10

        # If no carry, we're done - no need to process remaining digits
        if carry == 0:
            break

    # If there's still a carry after processing all digits
    # We need to add a new digit at the beginning
    if carry > 0:
        return [carry] + digits

    return digits


# Approach 3: Convert to Integer and Back (Not recommended for large numbers)
def plusOne_convert(digits):
    """
    This approach converts array to integer, adds 1, then converts back.
    WARNING: This approach has limitations with very large numbers due to integer overflow.
    Time Complexity: O(n) for conversion operations
    Space Complexity: O(n) for string operations
    """
    # Convert digits array to integer
    # Join all digits as string, then convert to int
    number = int(''.join(map(str, digits)))

    # Add 1 to the number
    number += 1

    # Convert back to list of digits
    # Convert to string, then split each character back to int
    return [int(digit) for digit in str(number)]


"""
ALGORITHM EXPLANATION:
================================================================
Steps for Simple Approach (Recommended):

1. Start from Rightmost Digit:
   - Begin iteration from the last index (rightmost digit)
   - This is the least significant digit where we add 1

2. Check Each Digit:
   - If digit < 9: Add 1 and return (no carry needed)
   - If digit = 9: Set it to 0 and continue left (carry over)

3. Handle All 9s Case:
   - If all digits were 9, we've set them all to 0
   - We need to prepend 1 to create the result
   - Example: [9,9] → [0,0] → [1,0,0]

Example Walkthrough for digits = [1,2,9]:
- i=2: digits[2]=9, set to 0, continue (carry over)
- i=1: digits[1]=2, add 1 to get 3, return [1,3,0]

Example Walkthrough for digits = [9,9,9]:
- i=2: digits[2]=9, set to 0, continue
- i=1: digits[1]=9, set to 0, continue  
- i=0: digits[0]=9, set to 0, continue
- All digits processed, array is [0,0,0]
- Return [1] + [0,0,0] = [1,0,0,0]

Learning Points:
================================================================
1. Array Traversal: Iterating backwards through an array using range(len-1, -1, -1)

2. Carry Logic: Understanding how mathematical carries work in addition
   - When digit + carry >= 10, we have a carry for the next position
   - Current digit becomes (digit + carry) % 10
   - Next carry becomes (digit + carry) // 10

3. Edge Case Handling: 
   - All digits being 9 requires creating a longer result array
   - Early termination when no carry is needed

4. In-place vs New Array:
   - We can modify the input array in-place for most cases
   - Only need new array when result has more digits than input

5. Mathematical Operations:
   - Modulo (%) for getting remainder (the digit to store)
   - Integer division (//) for getting quotient (the carry)

6. Array Manipulation:
   - Prepending elements to arrays: [new_element] + existing_array
   - List comprehension for transforming data

Key Takeaways for Future Problems:
================================================================
- Right-to-left processing is common in mathematical array problems
- Carry logic appears in addition, multiplication, and base conversion problems
- Consider edge cases where result size differs from input size
- Early termination can optimize performance when no further processing needed
- Be careful with integer overflow in conversion-based approaches
- In-place modification vs creating new arrays - consider space complexity

Applications in Other Problems:
- Add Binary (Leetcode 67)
- Multiply Strings (Leetcode 43) 
- Add Two Numbers (Leetcode 2)
- Any problem involving digit-by-digit arithmetic operations
"""

# Test the functions with various cases
if __name__ == "__main__":
    test_cases = [
        [1, 2, 3],  # Normal case
        [4, 3, 2, 1],  # Normal case
        [9],  # Single digit 9
        [9, 9],  # Multiple 9s
        [1, 9],  # Mixed with 9 at end
        [0],  # Single digit 0
    ]

    for digits in test_cases:
        # Make copies since some functions modify the input
        result1 = plusOne_simple(digits.copy())
        result2 = plusOne_with_carry(digits.copy())
        result3 = plusOne_convert(digits.copy())

        print(f"Input: {digits}")
        print(f"Simple: {result1}, Carry: {result2}, Convert: {result3}")
        print("-" * 50)