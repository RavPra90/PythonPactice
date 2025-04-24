"""
A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.
Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.

Example 1:
Input: arr = [3,5,1]
Output: true
Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.

Example 2:
Input: arr = [1,2,4]
Output: false
Explanation: There is no way to reorder the elements to obtain an arithmetic progression.
"""

def can_make_arithmetic_progression(arr):
    """
    Important Concept: Sorting + Constant Difference Check
    ------------------------------------------------------
    1. Sort the array: when arranged in order, an AP will have equal gaps.
    2. Compute the common difference using the first two elements.
    3. Verify that each subsequent gap equals the computed difference.
    """""

    # Step 1: Sort the array to bring numbers into increasing order
    sorted_arr = sorted(arr)
    print(f"Sorted array: {sorted_arr}")  # e.g. [1, 3, 5]

    # If there are fewer than 2 elements, it's trivially an AP
    if len(sorted_arr) < 2:
        print("Array has fewer than 2 elements: always an AP")
        return True

    # Step 2: Compute the common difference using the first pair
    common_diff = sorted_arr[1] - sorted_arr[0]
    print(f"Common difference (element[1] - element[0]): {common_diff}")  # e.g. 3 - 1 = 2

    # Step 3: Check each subsequent pair
    for i in range(2, len(sorted_arr)):
        current_diff = sorted_arr[i] - sorted_arr[i - 1]
        print(f"Check gap between {sorted_arr[i-1]} and {sorted_arr[i]}: {current_diff}")
        if current_diff != common_diff:
            print("Found a differing gap -> Not an AP")
            return False

    # If we finish the loop without mismatch, it's an AP
    print("All gaps equal -> Valid AP")
    return True


if __name__ == "__main__":
    # Example 1
    print("Example 1:")
    arr1 = [3, 5, 1]
    print(f"Input: {arr1}")
    result1 = can_make_arithmetic_progression(arr1)
    print(f"Output: {result1}\n")  # True

    # Example 2
    print("Example 2:")
    arr2 = [1, 2, 4]
    print(f"Input: {arr2}")
    result2 = can_make_arithmetic_progression(arr2)
    print(f"Output: {result2}\n")  # False

    # Additional Test: Negative and float values
    print("Additional Test (with negatives/floats):")
    arr3 = [2.5, -0.5, 1.5, 0.5]
    print(f"Input: {arr3}")
    result3 = can_make_arithmetic_progression(arr3)
    print(f"Output: {result3}\n")  # True  (Sequence: [-0.5, 0.5, 1.5, 2.5])

# Key Takeaways:
# - We sort the array to line up numbers in increasing order.
# - The first gap defines the "common difference."
# - By checking every adjacent gap, we ensure it's constant across the sequence.
# - Time Complexity: O(n log n) for sorting + O(n) for the check → O(n log n) overall.
# - Space Complexity: O(n) if sorting creates a new list, or O(1) extra if sorted in place.
# - Sorting is a powerful tool: it often simplifies pattern checks on sequences.

