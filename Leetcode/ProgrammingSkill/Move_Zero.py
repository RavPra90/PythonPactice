"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]
"""
def moveZeroes(nums: list[int]) -> None:
    """
    Move all 0’s in the list `nums` to the end, in-place, while keeping
    the relative order of the non-zero elements.

    Key concept for future learning: **Two-pointer technique**
    We use one pointer to scan through the array (`current`), and another
    pointer (`last_non_zero`) to track where the next non-zero element
    should go.

    Time Complexity: O(n) — we pass through the list just once.
    Space Complexity: O(1) — we do it in-place, with only two extra integer variables.
    """
    # Print initial state for clarity
    print("Initial array:", nums)

    # `last_non_zero` will point to the index where we should write
    # the next non-zero element we find.
    last_non_zero = 0

    # 1) First pass: move all non-zero elements forward, overwriting zeros.
    for current in range(len(nums)):
        print ("current",current)
        # If the current element is not zero, we want to keep it.
        if nums[current] != 0:
            # Debug print to illustrate what’s happening:
            print(f"nums[{current}] = {nums[current]} is non-zero.")
            print(f" → Placing it at index {last_non_zero}.")

            # Place nums[current] at the `last_non_zero` position.
            nums[last_non_zero] = nums[current]
            print(nums)

            # If current and last_non_zero differ, zero out the old spot
            # (this helps maintain correct values if we’re overwriting)
            if current != last_non_zero:
                nums[current] = 0
                print(f" → Setting nums[{current}] = 0 after moving.")

            # Move `last_non_zero` forward for the next non-zero element
            last_non_zero += 1

            # Show the array state after each non-zero move
            print(" Array now:", nums)

    # At this point, all non-zero elements are in front, and zeros have
    # been pushed back step by step.
    print("Final array with zeros moved:", nums)
    # No return needed because we modify `nums` in-place.


# --- Example runs ---

print("\nExample 1:")
nums1 = [0, 1, 0, 3, 12]
moveZeroes(nums1)
# Step-by-step prints:
# Initial array: [0, 1, 0, 3, 12]
# nums[0] = 0 → skip
# nums[1] = 1 → place at index 0, set nums[1]=0 → [1,0,0,3,12]
# nums[2] = 0 → skip
# nums[3] = 3 → place at index 1, set nums[3]=0 → [1,3,0,0,12]
# nums[4] = 12 → place at index 2, set nums[4]=0 → [1,3,12,0,0]
# Final array with zeros moved: [1,3,12,0,0]

print("\nExample 2:")
nums2 = [0]
moveZeroes(nums2)
# Initial array: [0]
# nums[0] = 0 → skip
# Final array with zeros moved: [0]

"""
================================================================================================================
================================================================================================================
"""

#ANOTHER APPROACH

def moveZeroes(nums: list[int]) -> None:
    """
    EASIER Pythonic method to move all zeros to the end in-place.

    Key concepts for future learning:
      • list.count(x): counts how many times x appears.
      • list comprehension: builds a new list based on a condition.
      • list concatenation (+) and repetition (*).
      • slice assignment (nums[:] = …) to modify the original list in-place.

    Steps (all in one go!):
    1. Count how many zeros are in nums.
    2. Build a list of only the non-zero elements.
    3. Recreate nums by combining:
         – the non-zero elements first, then
         – the right number of zeros at the end.
    4. Use slice assignment (nums[:]) so we don’t create a brand-new list object,
       but overwrite the original list’s contents.
    """

    # 1. Count zeros
    zero_count = nums.count(0)
    print(f"Count of zeros in the array: {zero_count}")

    # 2. Build a list of non-zero values
    non_zero_list = [x for x in nums if x != 0]
    print(f"List of non-zero elements: {non_zero_list}")

    # 3. Build the new sequence: non-zeros first, then zeros
    #    [0] * zero_count creates a list of zeros of the right length
    new_sequence = non_zero_list + [0] * zero_count
    print(f"Combined (non-zeros + zeros): {new_sequence}")

    # 4. Overwrite nums in-place so callers see the change
    nums[:] = new_sequence
    print(f"Final in-place modified array: {nums}")


# --- Example runs ---

print("Example 1:")
nums1 = [0, 1, 0, 3, 12]
print("Before:", nums1)
moveZeroes(nums1)
print("After: ", nums1)
# Expected Output: [1, 3, 12, 0, 0]

print("\nExample 2:")
nums2 = [0]
print("Before:", nums2)
moveZeroes(nums2)
print("After: ", nums2)
# Expected Output: [0]
