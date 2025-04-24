def judgeCircle(moves):
    """
    Determine if a robot, starting at (0, 0) on a 2D plane,
    returns to the origin after performing a sequence of moves.

    Parameters:
    - moves (str): A string where each character is one of:
        'U' = move up (y increases by 1)
        'D' = move down (y decreases by 1)
        'L' = move left (x decreases by 1)
        'R' = move right (x increases by 1)

    Returns:
    - bool: True if the robot ends at (0, 0), False otherwise.

    Important concepts:
    - Variables to hold state (x, y coordinates)
    - Looping over a string
    - Conditional statements to decide how to update state
    - Printing intermediate state for clarity
    - Boolean checks (x == 0 and y == 0)
    """

    # Start at the origin (0, 0)
    x, y = 0, 0
    print(f"Start at origin: (x, y) = ({x}, {y})\n")

    # Process each move one by one
    for step_number, move in enumerate(moves, start=1):
        # Check which direction to move and update x or y accordingly
        if move == 'U':
            y += 1            # Move up: increase y-coordinate by 1
        elif move == 'D':
            y -= 1            # Move down: decrease y-coordinate by 1
        elif move == 'L':
            x -= 1            # Move left: decrease x-coordinate by 1
        elif move == 'R':
            x += 1            # Move right: increase x-coordinate by 1
        else:
            # In well‑formed inputs, we shouldn't get here
            print(f"Warning: '{move}' is not a valid move")

        # Print the result of this step
        print(f"Step {step_number}: move='{move}' -> position now (x, y) = ({x}, {y})")

    # After all moves, check if we're back at the origin
    returned_to_origin = (x == 0 and y == 0)
    print(f"\nAfter all moves, final position: (x, y) = ({x}, {y})")
    print(f"Returned to origin? {'Yes' if returned_to_origin else 'No'}\n")

    return returned_to_origin


# --- Example usage with detailed outputs ---

if __name__ == "__main__":
    # Example 1: "UD"
    print("Example 1: moves = 'UD'")
    # Explanation:
    #  U moves from (0,0) to (0,1)
    #  D moves from (0,1) to (0,0)
    # final = origin → True
    result1 = judgeCircle("UD")
    print(f"Result: {result1}  # Expected: True\n{'-'*40}\n")

    # Example 2: "LL"
    print("Example 2: moves = 'LL'")
    # Explanation:
    #  L moves from (0,0) to (-1,0)
    #  L moves from (-1,0) to (-2,0)
    # final ≠ origin → False
    result2 = judgeCircle("LL")
    print(f"Result: {result2}  # Expected: False\n{'-'*40}\n")

    # You can try more cases:
    # e.g., "RUDL" should also return True because R→(1,0), U→(1,1), D→(1,0), L→(0,0)
    print("Example 3: moves = 'RUDL'")
    result3 = judgeCircle("RUDL")
    print(f"Result: {result3}  # Expected: True\n")


# Concepts highlighted for future learning:
# - **State Tracking**: Using variables (x, y) to remember where the robot is.
# - **Iteration**: Looping through each character in the 'moves' string.
# - **Conditionals**: Using if‑elif to decide how to change the state.
# - **String Indexing**: Reading each move from the string.
# - **Boolean Expressions**: Checking if (x, y) == (0, 0) to return True/False.
# - **Print Debugging**: Printing intermediate steps to understand how the algorithm works.
