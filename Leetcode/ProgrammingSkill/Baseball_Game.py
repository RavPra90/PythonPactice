def calPoints(ops):
    """
    Calculate the total score for a special baseball game.

    Rules:
    - You start with an empty record (a list of valid scores).
    - For each operation in ops:
        1. If it's an integer string "x", convert to int and append to record.
        2. If it's "+", append the sum of the last two scores.
        3. If it's "D", append double the last score.
        4. If it's "C", remove (invalidate) the last score.

    At the end, return the sum of all valid scores in the record.

    Important concepts:
    - Using a Python list as a stack: .append() to push, .pop() to remove.
    - List indexing: record[-1] for the most recent, record[-2] for the one before.
    - Converting strings to integers with int().
    - The built-in sum() function to total a list of numbers.
    """

    # Initialize an empty list to hold valid scores.
    record = []

    # Process each operation one by one
    for op in ops:
        # Case 1: Invalidate the previous score
        if op == "C":
            # .pop() removes and returns the last item in the list
            removed = record.pop()
            print(f"Operation 'C': removed previous score {removed}, record now: {record}")

        # Case 2: Double the previous score
        elif op == "D":
            last_score = record[-1]  # fetch the last score
            new_score = 2 * last_score  # double it
            record.append(new_score)  # push onto the record
            print(f"Operation 'D': doubled last score to {new_score}, record now: {record}")

        # Case 3: Sum of the previous two scores
        elif op == "+":
            score1 = record[-1]  # most recent
            score2 = record[-2]  # one before that
            new_score = score1 + score2  # sum them
            record.append(new_score)  # push onto the record
            print(f"Operation '+': summed {score2} + {score1} = {new_score}, record now: {record}")

        # Case 4: A new integer score
        else:
            # Convert string to integer (handles negatives automatically)
            score = int(op)
            record.append(score)  # push onto the record
            print(f"Operation '{op}': added new score {score}, record now: {record}")

    # After all operations, sum up the valid scores
    total_score = sum(record)
    print(f"Final record: {record}")
    print(f"Total score (sum of record): {total_score}\n")

    return total_score


# --- Example usages with expected outputs ---

if __name__ == "__main__":
    # Example 1
    ops1 = ["5", "2", "C", "D", "+"]
    # Step-by-step prints will show:
    # 5 added ⇒ [5]
    # 2 added ⇒ [5, 2]
    # C removes 2 ⇒ [5]
    # D doubles 5 ⇒ [5, 10]
    # + sums 5 and 10 ⇒ [5, 10, 15]
    # Sum ⇒ 30
    print("Example 1 result:", calPoints(ops1))  # Expected output: 30

    # Example 2
    ops2 = ["5", "-2", "4", "C", "D", "9", "+", "+"]
    # Walkthrough:
    # 5 ⇒ [5]
    # -2 ⇒ [5, -2]
    # 4 ⇒ [5, -2, 4]
    # C removes 4 ⇒ [5, -2]
    # D doubles -2 ⇒ [5, -2, -4]
    # 9 ⇒ [5, -2, -4, 9]
    # + sums -4 + 9 ⇒ [5, -2, -4, 9, 5]
    # + sums 9 + 5 ⇒ [5, -2, -4, 9, 5, 14]
    # Sum ⇒ 27
    print("Example 2 result:", calPoints(ops2))  # Expected output: 27

    # Example 3
    ops3 = ["1", "C"]
    # Walkthrough:
    # 1 ⇒ [1]
    # C removes 1 ⇒ []
    # Sum ⇒ 0
    print("Example 3 result:", calPoints(ops3))  # Expected output: 0

# Concepts highlighted for future learning:
# - List operations: append(), pop(), indexing with negative indices
# - Type conversion: int("123") ⇒ 123
# - Control flow: if-elif-else blocks
# - Iteration: for loops over lists
# - Built-in functions: sum(), print()
