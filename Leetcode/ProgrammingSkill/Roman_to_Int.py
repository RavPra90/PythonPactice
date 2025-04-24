"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.


Example 1:
Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

"""


def roman_to_int(s):
    """
    Converts a Roman numeral string to an integer.
    
    Approach:
    1. Create a dictionary to map Roman symbols to their integer values.
    2. Iterate through each character in the string.
    3. For each character, check if the next character has a higher value:
       - If yes, subtract the current value (subtractive case like IV or IX).
       - If no, add the current value.
    4. Return the accumulated total.

    Examples:
    - Input: "III" → Output: 3 (1 + 1 + 1)
    - Input: "IX" → Output: 9 (10 - 1)
    - Input: "MCMXCIV" → Output: 1994 (1000 - 100 + 1000 - 10 + 100 - 1 + 5)
    """""
    # Step 1: Define mapping from Roman symbols to integer values
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    print(f"Roman mapping: {roman_map}\n")  # Show the basic symbol-value map

    total = 0  # This will accumulate our result
    n = len(s)  # Length of the input string
    print("length", n)
    # Step 2: Process each symbol, with lookahead for subtraction cases
    for i in range(n):
        # Current value from map
        current_val = roman_map[s[i]]

        # Look ahead: if this is not the last symbol,
        # get the next symbol's value
        if i + 1 < n:
            next_val = roman_map[s[i + 1]]
        else:
            next_val = 0  # No next symbol, so treat as 0

        # Debug: show what we're comparing
        print(f"At index {i}: symbol={s[i]}, value={current_val}")
        if next_val > current_val:
            # Subtraction case
            print(f"  Next symbol is {s[i+1]} with value {next_val} > {current_val}, so subtract {current_val}")
            total -= current_val
        else:
            # Normal addition case
            print(f"  Next symbol {'exists' if next_val else 'does not exist or is smaller'}, so add {current_val}")
            total += current_val
        print(f"  Running total: {total}\n")

    # Step 3: After the loop, total holds the integer value
    print(f"Final result for {s}: {total}\n")
    return total

if __name__ == "__main__":
    # Example 1
    print("Example 1:")
    s1 = "III"
    print(f"Input: {s1}")
    print(f"Output: {roman_to_int(s1)}")
    # Expected: 3 (I + I + I)
    print("---\n")

    # Example 2
    print("Example 2:")
    s2 = "LVIII"
    print(f"Input: {s2}")
    print(f"Output: {roman_to_int(s2)}")
    # Explanation: L (50) + V (5) + III (3) = 58
    print("---\n")

    # Example 3
    print("Example 3:")
    s3 = "MCMXCIV"
    print(f"Input: {s3}")
    print(f"Output: {roman_to_int(s3)}")
    # Explanation: M (1000) + CM (900) + XC (90) + IV (4) = 1994
    print("---\n")

# Key Takeaways:
# - We use a dictionary (hash map) to map characters to values in O(1) time.
# - The "lookahead subtraction" trick handles cases like IV, IX, etc.
# - Time Complexity: O(n) because we traverse the string once.
# - Space Complexity: O(1) extra space (only fixed-size map and counters).
# - Mapping and lookahead are powerful patterns for symbol-based parsing.


