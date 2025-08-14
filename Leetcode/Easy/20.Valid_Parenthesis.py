"""
LEETCODE PROBLEM: 20. Valid Parentheses
========================================
Problem Statement:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Example:
Input: s = "()[]{}"
Output: true

Input: s = "([)]"
Output: false

Input: s = "{[]}"
Output: true
"""


# Approach to solve the problem
def isValid(s):
    """
    ALGORITHM EXPLANATION:
    ================================================================
    Steps:
    1. Use a stack (list) to keep track of opening brackets
    2. Create a mapping of closing brackets to their corresponding opening brackets
    3. Iterate through each character in the string:
       - If it's an opening bracket: push it onto the stack
       - If it's a closing bracket: check if it matches the most recent opening bracket
    4. If stack is empty at the end, all brackets were properly matched

    Learning:
    - Stack Data Structure: Perfect for matching/pairing problems (LIFO - Last In, First Out)
    - Hash Map Usage: Quick lookup for bracket pairs using dictionary
    - Early Exit Pattern: Return False immediately when mismatch is found
    - Edge Case Handling: Empty stack, unmatched brackets
    - String Traversal: Process each character systematically
    - Validation Logic: Check conditions step by step before concluding
    """

    # Create a stack to store opening brackets
    # We'll use a Python list as a stack (append = push, pop = pop)
    stack = []

    # Create a mapping of closing brackets to opening brackets
    # This allows quick lookup: given a closing bracket, what opening bracket should match?
    bracket_map = {
        ')': '(',  # closing parenthesis maps to opening parenthesis
        '}': '{',  # closing brace maps to opening brace
        ']': '['  # closing bracket maps to opening bracket
    }

    # Process each character in the input string
    for char in s:
        # Check if current character is a closing bracket
        if char in bracket_map:
            # We found a closing bracket, so we need to check if it matches
            # the most recent opening bracket (top of stack)

            # First, check if stack is empty (no opening bracket to match)
            if not stack:
                return False  # Closing bracket with no matching opening bracket

            # Pop the most recent opening bracket from stack
            top_element = stack.pop()

            # Check if the popped opening bracket matches the current closing bracket
            if bracket_map[char] != top_element:
                return False  # Mismatched pair (e.g., '(' with '}')

        else:
            # Current character is an opening bracket
            # Push it onto the stack to wait for its matching closing bracket
            stack.append(char)

    # After processing all characters, check if stack is empty
    # Empty stack means all opening brackets found their matching closing brackets
    # Non-empty stack means some opening brackets were never closed
    return len(stack) == 0


# Example walkthrough with s = "([{}])"
"""
STEP-BY-STEP WALKTHROUGH:
========================
Input: s = "([{}])"
stack = [], bracket_map = {')': '(', '}': '{', ']': '['}

char = '(': Opening bracket → stack.append('(') → stack = ['(']
char = '[': Opening bracket → stack.append('[') → stack = ['(', '[']
char = '{': Opening bracket → stack.append('{') → stack = ['(', '[', '{']
char = '}': Closing bracket → char in bracket_map = True
           → stack not empty ✓
           → top_element = stack.pop() = '{' → stack = ['(', '[']
           → bracket_map['}'] = '{', top_element = '{' → Match ✓
char = ']': Closing bracket → char in bracket_map = True
           → stack not empty ✓
           → top_element = stack.pop() = '[' → stack = ['(']
           → bracket_map[']'] = '[', top_element = '[' → Match ✓
char = ')': Closing bracket → char in bracket_map = True
           → stack not empty ✓
           → top_element = stack.pop() = '(' → stack = []
           → bracket_map[')'] = '(', top_element = '(' → Match ✓

Final check: len(stack) == 0? YES → Return True

Example with invalid input "([)]":
========================
char = '(': stack = ['(']
char = '[': stack = ['(', '[']
char = ')': top_element = '[', bracket_map[')'] = '('
           → '[' != '(' → Return False (mismatch!)
"""


# Alternative solution using only opening brackets check
def isValidAlternative(s):
    """
    Alternative approach: Check for opening brackets directly
    This version might be slightly more readable for beginners
    """
    stack = []

    for char in s:
        # If opening bracket, push it to stack
        if char in '({[':
            stack.append(char)
        # If closing bracket, check for match
        elif char in ')}]':
            # No opening bracket to match
            if not stack:
                return False

            # Get the last opening bracket
            last_open = stack.pop()

            # Check if they form a valid pair
            if (char == ')' and last_open != '(') or \
                    (char == '}' and last_open != '{') or \
                    (char == ']' and last_open != '['):
                return False

    # All brackets matched if stack is empty
    return len(stack) == 0


# Test cases to verify the solution
test_cases = [
    "()",  # True - simple pair
    "()[]{}",  # True - multiple pairs
    "(]",  # False - mismatch
    "([)]",  # False - wrong order
    "{[]}",  # True - nested pairs
    "",  # True - empty string
    "(((",  # False - unmatched opening
    ")))",  # False - unmatched closing
]

# Uncomment to test:
# for test in test_cases:
#     result = isValid(test)
#     print("Input: '" + test + "' -> " + str(result))