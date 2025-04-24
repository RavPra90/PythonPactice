"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Example 2:
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

Example 3:
Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
"""

def plus_one(nums):
    x = int(''.join(str(d) for d in nums))
    x +=1
    print(x)
    l= [int(d) for d in str(x)]
    print(l)

plus_one([1,2,3])
plus_one([9])

"""
================================================================================================================
==============================================================================================================
"""
"""
Carry Propagation
The traditional approach avoids converting the entire number 
and works digit-by-digit from the back, mimicking how addition is done by hand. 
It scales better for extremely large numbers.
"""


def plus_one(digits):
    """
      Important Concept: Carry Propagation
       ------------------------------------
       When adding 1 to the last digit causes it to become 10, we set it to 0 and "carry" 1 to the next digit.
       This process continues until there's no carry left or we reach the most significant digit.
       If we still have a carry after processing the most significant digit, we insert a new digit at the front.

      """""
    n = len(digits)
    print("length : ",n)
    carry = 1  # we want to add 1 to the number

    # Process each digit from right to left
    for i in range(n - 1, -1, -1):
        print(f"i: {i} , value {digits[i]}")
        old_value = digits[i]
        new_value = old_value + carry
        # Compute digit to store and new carry
        digits[i] = new_value % 10  # % 10 gives the remainder (0-9)
        carry = new_value // 10     # // 10 gives how many tens we have (0 or 1 here)

        # Debug output to show what's happening at each step
        print(f"Step {n - i}: Adding carry, old digit = {old_value}, new digit = {digits[i]}, carry = {carry}")

        # If there's no carry, we can stop early
        if carry == 0:
            break

    # If carry is still 1 after the loop, we need to add a new most significant digit
    if carry:
        print("Carry remains after processing all digits, inserting 1 at the front")
        digits.insert(0, 1)

    return digits

if __name__ == "__main__":
    # Example 1
    print("Example 1:")
    input_digits = [1, 2, 3]
    print(f"Input: {input_digits}")
    result = plus_one(input_digits.copy())
    print(f"Output: {result}\n")

    # Example 2
    print("Example 2:")
    input_digits = [4, 3, 2, 1]
    print(f"Input: {input_digits}")
    result = plus_one(input_digits.copy())
    print(f"Output: {result}\n")

    # Example 3
    print("Example 3:")
    input_digits = [9]
    print(f"Input: {input_digits}")
    result = plus_one(input_digits.copy())
    print(f"Output: {result}\n")

    # Additional test: multiple carries
    print("Additional Test (multiple carries):")
    input_digits = [9, 9, 9]
    print(f"Input: {input_digits}")
    result = plus_one(input_digits.copy())
    print(f"Output: {result}\n")

# Key Takeaways:
# - We traverse the list from least significant to most significant digit.
# - Use modulo (%) to extract the new digit and integer division (//) to compute carry.
# - Early exit if carry becomes zero to save time.
# - If carry remains after the most significant digit, insert a new digit at the front.
# - Time Complexity: O(n) where n is the number of digits.
# - Space Complexity: O(1) extra space (modifying in place), plus O(n) in worst case when inserting at front.
