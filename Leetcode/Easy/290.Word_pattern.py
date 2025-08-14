"""
LEETCODE PROBLEM: 290. Word Pattern
========================================
Problem Statement:
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter 
in pattern and a non-empty word in s.

Example:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Explanation: There's a bijection: 'a' maps to "dog", 'b' maps to "cat"

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Explanation: 'a' should map to the same word, but maps to both "dog" and "fish"

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
Explanation: 'a' maps to multiple different words
"""


# Approach to solve the problem: Hash Map Bidirectional Mapping
def wordPattern(pattern, s):
    """
    Check if string s follows the same pattern using bidirectional mapping.

    Args:
        pattern (str): The pattern string containing letters
        s (str): The string containing words separated by spaces

    Returns:
        bool: True if s follows the pattern, False otherwise
    """
    # Split the string s into individual words
    words = s.split()

    # Early check: pattern length must equal number of words
    if len(pattern) != len(words):
        return False

    # Create two hash maps for bidirectional mapping
    # char_to_word: maps each character in pattern to a word
    # word_to_char: maps each word to a character in pattern
    char_to_word = {}
    word_to_char = {}

    # Iterate through pattern and words simultaneously
    for i in range(len(pattern)):
        char = pattern[i]
        word = words[i]

        # Check if character already has a mapping
        if char in char_to_word:
            # If character maps to a different word, pattern is broken
            if char_to_word[char] != word:
                return False
        else:
            # Create new mapping from character to word
            char_to_word[char] = word

        # Check if word already has a mapping
        if word in word_to_char:
            # If word maps to a different character, pattern is broken
            if word_to_char[word] != char:
                return False
        else:
            # Create new mapping from word to character
            word_to_char[word] = char

    # If we've successfully created consistent bidirectional mappings, return True
    return True


"""
ALGORITHM EXPLANATION:
================================================================
Steps:
1. Split the input string into individual words
2. Check if the number of characters in pattern equals number of words
3. Create two hash maps for bidirectional mapping:
   - char_to_word: ensures each character maps to only one word
   - word_to_char: ensures each word maps to only one character
4. Iterate through pattern and words simultaneously:
   - For each character-word pair, check existing mappings
   - If mapping exists and conflicts, return False
   - If no mapping exists, create new mapping
5. Return True if all mappings are consistent

Time Complexity: O(n) where n is the length of pattern (or number of words)
Space Complexity: O(n) for storing the mappings in hash maps

Learning:
- Bidirectional Mapping: Using two hash maps to ensure one-to-one correspondence
- Hash Map Usage: Efficient lookup and storage for key-value relationships
- String Processing: Splitting strings and handling word boundaries
- Pattern Matching: Understanding bijective relationships (one-to-one mapping)
- Early Termination: Checking length mismatch before processing
- Validation Logic: Ensuring consistency in both directions of mapping

Why Two Hash Maps?
- One map alone isn't sufficient because we need to ensure BOTH:
  1. Each character maps to exactly one word
  2. Each word maps to exactly one character
- This prevents cases like: pattern="ab", s="dog dog" (different chars, same word)

Example Walkthrough:
pattern = "abba", s = "dog cat cat dog"

Step 1: words = ["dog", "cat", "cat", "dog"]
Step 2: len(pattern) = 4, len(words) = 4 ✓

Iteration:
i=0: char='a', word="dog"
  - char_to_word: {} → {'a': 'dog'}
  - word_to_char: {} → {'dog': 'a'}

i=1: char='b', word="cat"
  - char_to_word: {'a': 'dog'} → {'a': 'dog', 'b': 'cat'}
  - word_to_char: {'dog': 'a'} → {'dog': 'a', 'cat': 'b'}

i=2: char='b', word="cat"
  - char_to_word['b'] = "cat" ✓ (matches current word)
  - word_to_char["cat"] = 'b' ✓ (matches current char)

i=3: char='a', word="dog"
  - char_to_word['a'] = "dog" ✓ (matches current word)
  - word_to_char["dog"] = 'a' ✓ (matches current char)

Result: All mappings consistent → Return True

Counter Example:
pattern = "abba", s = "dog cat cat fish"

i=3: char='a', word="fish"
  - char_to_word['a'] = "dog" ≠ "fish" ✗
  - Return False (character 'a' trying to map to two different words)
"""


# Test cases to verify the solution
def test_solution():
    # Test case 1: Valid pattern
    assert wordPattern("abba", "dog cat cat dog") == True

    # Test case 2: Character maps to multiple words
    assert wordPattern("abba", "dog cat cat fish") == False

    # Test case 3: Multiple characters map to same word
    assert wordPattern("aaaa", "dog cat cat dog") == False

    # Test case 4: Length mismatch
    assert wordPattern("abba", "dog cat cat") == False

    # Test case 5: Single character pattern
    assert wordPattern("a", "dog") == True