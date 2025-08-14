"""
LEETCODE PROBLEM: 205. Isomorphic Strings
========================================
Problem Statement:
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with the same character while
preserving the order of characters. No two characters may map to the same character,
but a character may map to itself.

Example:
Input: s = "egg", t = "add"
Output: true
Explanation: 'e' maps to 'a', 'g' maps to 'd'

Input: s = "foo", t = "bar"
Output: false
Explanation: 'o' cannot map to both 'a' and 'r'

Input: s = "paper", t = "title"
Output: true
Explanation: 'p'→'t', 'a'→'i', 'p'→'t', 'e'→'l', 'r'→'e'
"""


# Approach to solve the problem: Bidirectional Character Mapping
def isIsomorphic(s, t):
    """
    Check if two strings are isomorphic using bidirectional character mapping.

    Args:
        s (str): First string
        t (str): Second string

    Returns:
        bool: True if strings are isomorphic, False otherwise
    """
    # If strings have different lengths, they can't be isomorphic
    if len(s) != len(t):
        return False

    # Create two hash maps for bidirectional mapping
    # s_to_t: maps each character in s to corresponding character in t
    # t_to_s: maps each character in t to corresponding character in s
    s_to_t = {}
    t_to_s = {}

    # Iterate through both strings simultaneously
    for i in range(len(s)):
        char_s = s[i]  # Current character from string s
        char_t = t[i]  # Current character from string t

        # Check mapping from s to t
        if char_s in s_to_t:
            # If char_s already has a mapping, it must map to the same char_t
            if s_to_t[char_s] != char_t:
                return False
        else:
            # Create new mapping from char_s to char_t
            s_to_t[char_s] = char_t

        # Check mapping from t to s (reverse direction)
        if char_t in t_to_s:
            # If char_t already has a mapping, it must map to the same char_s
            if t_to_s[char_t] != char_s:
                return False
        else:
            # Create new mapping from char_t to char_s
            t_to_s[char_t] = char_s

    # If we successfully created consistent bidirectional mappings, strings are isomorphic
    return True


# Alternative approach using transformation pattern
def isIsomorphic_alternative(s, t):
    """
    Alternative solution using character position transformation.

    The idea is to transform both strings into the same pattern based on
    when each character first appears.
    """

    def get_pattern(string):
        """Convert string to pattern based on first occurrence of characters"""
        char_to_index = {}
        pattern = []

        for i, char in enumerate(string):
            if char not in char_to_index:
                # First time seeing this character, assign it the current index
                char_to_index[char] = i
            # Add the first occurrence index to pattern
            pattern.append(char_to_index[char])

        return pattern

    # Two strings are isomorphic if they have the same transformation pattern
    return get_pattern(s) == get_pattern(t)


"""
ALGORITHM EXPLANATION:
================================================================
Steps (Main Solution):
1. Check if both strings have the same length (prerequisite for isomorphism)
2. Create two hash maps for bidirectional character mapping:
   - s_to_t: ensures each character in s maps to exactly one character in t
   - t_to_s: ensures each character in t maps to exactly one character in s
3. Iterate through both strings character by character:
   - For each position, get characters from both strings
   - Check if current character in s already has a mapping in s_to_t
   - If yes, verify it matches current character in t; if no, return False
   - If no mapping exists, create new mapping
   - Repeat the same process for reverse mapping (t_to_s)
4. Return True if all character pairs create consistent bidirectional mappings

Time Complexity: O(n) where n is the length of the strings
Space Complexity: O(k) where k is the number of unique characters (at most O(n))

Learning:
- Bidirectional Mapping: Critical pattern for ensuring one-to-one relationships
- Hash Map Applications: Using multiple hash maps to validate different constraints
- Character Mapping: Understanding how to create and validate character transformations
- Pattern Recognition: Two strings are isomorphic if they follow the same structural pattern
- Edge Case Handling: Always check string lengths first for string comparison problems
- Alternative Approaches: Same problem can be solved using pattern transformation
- Constraint Validation: Ensuring no character maps to multiple different characters

Why Bidirectional Mapping is Necessary:
- Forward mapping (s→t) ensures each character in s maps to only one character in t
- Reverse mapping (t→s) ensures no two characters in s map to the same character in t
- Both constraints together guarantee true isomorphism (bijective mapping)

Example Walkthrough:
s = "egg", t = "add"

Iteration:
i=0: char_s='e', char_t='a'
  - s_to_t: {} → {'e': 'a'}
  - t_to_s: {} → {'a': 'e'}

i=1: char_s='g', char_t='d'
  - s_to_t: {'e': 'a'} → {'e': 'a', 'g': 'd'}
  - t_to_s: {'a': 'e'} → {'a': 'e', 'd': 'g'}

i=2: char_s='g', char_t='d'
  - s_to_t['g'] = 'd' ✓ (matches current char_t)
  - t_to_s['d'] = 'g' ✓ (matches current char_s)

Result: All mappings consistent → Return True

Counter Example:
s = "foo", t = "bar"

i=0: char_s='f', char_t='b' → Create mappings
i=1: char_s='o', char_t='a' → Create mappings  
i=2: char_s='o', char_t='r'
  - s_to_t['o'] = 'a' ≠ 'r' ✗
  - Return False ('o' trying to map to two different characters)

Alternative Pattern Approach Example:
s = "egg" → pattern: [0, 1, 1] (e appears at index 0, g appears at index 1)
t = "add" → pattern: [0, 1, 1] (a appears at index 0, d appears at index 1)
Since patterns match, strings are isomorphic.
"""


# Test cases to verify the solution
def test_solution():
    # Test case 1: Basic isomorphic strings
    assert isIsomorphic("egg", "add") == True

    # Test case 2: Non-isomorphic - character maps to multiple
    assert isIsomorphic("foo", "bar") == False

    # Test case 3: Longer isomorphic strings
    assert isIsomorphic("paper", "title") == True

    # Test case 4: Same characters mapping to themselves
    assert isIsomorphic("ab", "aa") == False

    # Test case 5: Empty strings
    assert isIsomorphic("", "") == True

    # Test case 6: Single characters
    assert isIsomorphic("a", "b") == True

    # Verify alternative solution gives same results
    assert isIsomorphic_alternative("egg", "add") == True
    assert isIsomorphic_alternative("foo", "bar") == False