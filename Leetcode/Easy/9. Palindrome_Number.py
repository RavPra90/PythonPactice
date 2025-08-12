"""
LEETCODE PROBLEM: 9. Palindrome Number
========================================
Problem Statement:
Given an integer x, return true if x is a palindrome integer.
An integer is a palindrome when it reads the same backward as forward.

Example:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""


# Approach 1: Convert to String (Easier to understand)
def isPalindrome_string_approach(x):
    """
    This approach converts the number to a string and checks if it reads the same forwards and backwards.
    Time Complexity: O(log n) where n is the input number
    Space Complexity: O(log n) for storing the string
    """
    # Convert the integer to string
    str_x = str(x)

    # Compare the string with its reverse
    # str_x[::-1] creates a reversed version of the string
    return str_x == str_x[::-1]


# Approach 2: Mathematical Approach (More efficient, no extra space for string)
def isPalindrome_math_approach(x):
    """
    This approach reverses the number mathematically and compares it with the original.
    Time Complexity: O(log n) where n is the input number
    Space Complexity: O(1) - constant space
    """
    # Negative numbers are never palindromes
    if x < 0:
        return False

    # Single digit numbers are always palindromes
    if x < 10:
        return True

    # Numbers ending with 0 (except 0 itself) are never palindromes
    # Example: 10, 100, 1000 etc. cannot be palindromes
    if x % 10 == 0:
        return False

    # Store the original number for comparison
    original = x
    reversed_num = 0

    # Reverse the number digit by digit
    while x > 0:
        # Get the last digit of x
        last_digit = x % 10

        # Add this digit to our reversed number
        # Multiply by 10 to shift existing digits left, then add new digit
        reversed_num = reversed_num * 10 + last_digit

        # Remove the last digit from x
        x = x // 10

    # Check if original number equals reversed number
    return original == reversed_num


# Approach 3: Optimized Mathematical Approach (Reverse only half the number)
def isPalindrome_optimized(x):
    """
    This approach only reverses half of the number to save time and space.
    We compare the first half with the reversed second half.
    Time Complexity: O(log n) where n is the input number
    Space Complexity: O(1) - constant space
    """
    # Negative numbers and numbers ending with 0 (except 0) are not palindromes
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    reversed_half = 0

    # Continue until we've processed half the digits
    # When x becomes less than or equal to reversed_half, we've reached the middle
    while x > reversed_half:
        # Take the last digit from x and add it to reversed_half
        reversed_half = reversed_half * 10 + x % 10
        # Remove the last digit from x
        x //= 10

    # For even number of digits: x should equal reversed_half
    # For odd number of digits: x should equal reversed_half//10
    # (because the middle digit doesn't need to be checked)
    return x == reversed_half or x == reversed_half // 10


"""
ALGORITHM EXPLANATION:
================================================================
Steps for Mathematical Approach (Approach 2):

1. Handle Edge Cases:
   - Negative numbers: Always return False (they can't be palindromes)
   - Single digits: Always return True (0-9 are palindromes)
   - Numbers ending with 0: Return False (except for 0 itself)

2. Reverse the Number:
   - Use modulo (%) to get the last digit
   - Use integer division (//) to remove the last digit
   - Build the reversed number by multiplying by 10 and adding the new digit

3. Compare:
   - Check if the original number equals the reversed number

Example Walkthrough for x = 121:
- original = 121, reversed_num = 0
- Iteration 1: last_digit = 1, reversed_num = 0*10 + 1 = 1, x = 12
- Iteration 2: last_digit = 2, reversed_num = 1*10 + 2 = 12, x = 1  
- Iteration 3: last_digit = 1, reversed_num = 12*10 + 1 = 121, x = 0
- Compare: 121 == 121 → True

Learning Points:
================================================================
1. String Manipulation: Converting numbers to strings for easy reversal
2. Mathematical Operations: Using modulo (%) and integer division (//) to extract digits
3. Edge Case Handling: Considering negative numbers, single digits, and trailing zeros
4. Optimization: The half-reversal approach reduces time complexity
5. Multiple Solution Approaches: Same problem can be solved in different ways with different trade-offs
6. Time vs Space Complexity: String approach uses more space but is easier to understand

Key Takeaways for Future Problems:
- Always consider edge cases first
- Mathematical approaches often use less space than string conversions
- Digit manipulation using % and // is a common technique in number-based problems
- Sometimes you can optimize by processing only part of the data (half-reversal approach)
"""

# Test the functions
if __name__ == "__main__":
    test_cases = [121, -121, 10, 0, 1, 1221, 12321]

    for num in test_cases:
        result1 = isPalindrome_string_approach(num)
        result2 = isPalindrome_math_approach(num)
        result3 = isPalindrome_optimized(num)
        print(f"x = {num}: String={result1}, Math={result2}, Optimized={result3}")