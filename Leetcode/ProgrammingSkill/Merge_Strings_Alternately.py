"""
Example 1:
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r


Example 2:
Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b
word2:    p   q   r   s
merged: a p b q   r   s

Example 3:
Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q
merged: a p b q c   d
"""

from itertools import zip_longest  # Import zip_longest to handle uneven lengths in iteration

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        --- Important Concept ---
         We are using zip_longest from itertools which allows us to iterate over two lists (or strings) at the same time.
         Unlike the regular zip(), zip_longest() continues until the longest iterable is exhausted.
         It fills the missing values with a specified fillvalue, which we set to an empty string ('') to avoid adding unwanted characters.

         Step 1: Create an empty list to hold the merged characters.
         Lists are used because appending to a list is more efficient than using string concatenation in a loop.
        """

        merged = []

        # Step 2: Use zip_longest to iterate over both strings together
        for c1, c2 in zip_longest(word1, word2, fillvalue=''):
            """
             Example: word1 = "abc", word2 = "pqr"
             Iteration 1: c1 = 'a', c2 = 'p' → merged = ['a', 'p']
             Iteration 2: c1 = 'b', c2 = 'q' → merged = ['a', 'p', 'b', 'q']
             Iteration 3: c1 = 'c', c2 = 'r' → merged = ['a', 'p', 'b', 'q', 'c', 'r']
             
            """
            # Append the character from word1 (or '' if exhausted)
            merged.append(c1)

            # Append the character from word2 (or '' if exhausted)
            merged.append(c2)

        # Step 3: Join the list into a single string
        # ''.join([...]) efficiently combines list elements into a string
        # Example: ['a', 'p', 'b', 'q', 'c', 'r'] → 'apbqcr'
        return ''.join(merged)

# --- Example usage to demonstrate behavior ---
if __name__ == "__main__":
    sol = Solution()

    # Example 1: Strings of equal length
    # word1 = "abc", word2 = "pqr" → output = "apbqcr"
    print(sol.mergeAlternately("abc",  "pqr"))   # Expected: 'apbqcr'

    # Example 2: Second string is longer
    # word1 = "ab", word2 = "pqrs" → output = "apbqrs"
    # Explanation:
    # Iteration 1: 'a' + 'p'
    # Iteration 2: 'b' + 'q'
    # Remaining: 'r', 's' from word2
    print(sol.mergeAlternately("ab",   "pqrs"))  # Expected: 'apbqrs'

    # Example 3: First string is longer
    # word1 = "abcd", word2 = "pq" → output = "apbqcd"
    # Explanation:
    # Iteration 1: 'a' + 'p'
    # Iteration 2: 'b' + 'q'
    # Remaining: 'c', 'd' from word1
    print(sol.mergeAlternately("abcd", "pq"))    # Expected: 'apbqcd'

# --- Summary for Future Learning ---
# 1. Use zip_longest() to handle uneven iterables.
# 2. Lists are efficient for building up strings before joining.
# 3. The empty string ('') as fillvalue ensures clean merging.
# 4. Always join the list into a string at the end for final output.


#Another Approach Pure‑Python manual loop (no itertools)

class Solution2(object):
    def mergeAlternately(self, word1, word2):
        merged = []
        max_len = max(len(word1), len(word2))
        for i in range(max_len):
            if i < len(word1):
                merged.append(word1[i])
            if i < len(word2):
                merged.append(word2[i])
        return ''.join(merged)