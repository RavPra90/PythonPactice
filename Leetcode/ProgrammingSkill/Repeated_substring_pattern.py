"""
Given a string s, check if it can be constructed by taking a substring of it
 and appending multiple copies of the substring together.
Example 1:
Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.

Example 2:
Input: s = "aba"
Output: false
Example 3:

Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.

"""


def repeatedSubstringPattern(s: str) -> bool:
    """
    Determine if the string `s` can be built by repeating one of its substrings.

    Key idea (important concept!):
    - If `s` has length `n`, and it is made by repeating a substring of length `l`,
      then `l` must divide `n` exactly (n % l == 0).
    - We can “try out” every possible substring length `l` from 1 up to n//2.
    - For each `l`, take the first `l` characters (s[:l]), repeat that chunk n//l times,
      and see if it recreates the original string.

    Time complexity: O(n^2) in the worst case (for each l we build and compare an O(n) string).
    """

    n = len(s)
    print(f"Input string: '{s}' (length = {n})\n")

    # We only need to check lengths up to n//2, since a substring longer than half
    # would repeat fewer than two times and can't form the full string.
    for l in range(1, n // 2 + 1):
        # Only consider lengths that divide n evenly
        if n % l == 0:
            # Extract the candidate substring of length l
            substring = s[:l]
            repeat_count = n // l

            # Build a string by repeating the candidate substring
            built = substring * repeat_count

            # Show step-by-step for learning
            print(f"Trying l = {l}:")
            print(f"  substring = s[:{l}] = '{substring}'")
            print(f"  repeat_count = {repeat_count}")
            print(f"  built = '{substring}' * {repeat_count} = '{built}'")

            # If the built-up string matches s, we found our repeating pattern
            if built == s:
                print("  → Match found! Returning True.\n")
                return True
            else:
                print("  → No match; trying next length.\n")

    # If no possible substring worked, return False
    print("No repeating substring pattern found. Returning False.\n")
    return False


# --- Example runs ---

print("Example 1: s = 'abab'")
print("Output:", repeatedSubstringPattern("abab"))
# Explanation in code:
# - length n = 4
# - l = 1 → substring 'a', built = 'aaaa' → no
# - l = 2 → substring 'ab', built = 'abab' → yes → True

print("Example 2: s = 'aba'")
print("Output:", repeatedSubstringPattern("aba"))
# Explanation in code:
# - length n = 3
# - l = 1 → substring 'a', built = 'aaa' → no
# - (n//2 = 1, so only l=1 was tried) → False

print("Example 3: s = 'abcabcabcabc'")
print("Output:", repeatedSubstringPattern("abcabcabcabc"))
# Explanation in code:
# - n = 12
# - l = 1 → 'a' *12 = 'aaaaaaaaaaaa' → no
# - l = 2 → 'ab' *6 = 'abababababab' → no
# - l = 3 → 'abc' *4 = 'abcabcabcabc' → yes → True

"""

===============================================================================================================\
=================================================================================================================

"""
# ANother Approach

def repeatedSubstringPattern2(s: str) -> bool:
    """
    Check if `s` can be formed by repeating a substring of itself.

    Easier (and faster!) trick:
      - Take the string `s` and concatenate it with itself: `s + s`.
      - Remove the first and last character of that doubled string.
      - If the original `s` still appears as a substring inside this modified string,
        then `s` must be made of a repeating pattern.

    Why this works:
      • If `s = 'abab'`, doubling gives 'abababab'.
        Removing first and last chars → 'bababa b'.
        'abab' appears in the middle: 'ba[abab]ab'.
      • If `s = 'aba'`, doubling gives 'abaaba'.
        Removing first/last → 'baab'.
        'aba' does NOT appear in 'baab', so no pattern.

    Key concept for future:
      – String concatenation & slicing
      – Substring search in O(n) with built-in methods
    """

    # 1. Quick reject for empty string
    if not s:
        return False

    # 2. Build the modified doubled string
    doubled = s + s  # e.g. 'abab' -> 'abababab'
    middle = doubled[1:-1]  # remove first & last char -> 'bababa'

    # Debug prints to illustrate (optional for learning)
    print(f"Original:    '{s}'")
    print(f"Doubled:     '{doubled}'")
    print(f"Middle part: '{middle}'")

    # 3. Check if original s exists in the middle part
    return s in middle


# --- Examples ---

print(repeatedSubstringPattern2("abab"))
# Steps shown:
# Original:    'abab'
# Doubled:     'abababab'
# Middle part: 'bababa'
# Does 'abab' appear? Yes → True

print(repeatedSubstringPattern2("aba"))
# Original:    'aba'
# Doubled:     'abaaba'
# Middle part: 'baab'
# Does 'aba' appear? No → False

print(repeatedSubstringPattern2("abcabcabcabc"))
# Original:    'abcabcabcabc'
# Doubled:     'abcabcabcabcabcabcabcabc'
# Middle part: 'bcabcabcabcabcabcabcab'
# Does original appear? Yes → True
