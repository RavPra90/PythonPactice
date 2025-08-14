"""
LEETCODE PROBLEM: 141. Linked List Cycle
========================================
Problem Statement:
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached
again by continuously following the next pointer. Internally, pos is used to denote the
index of the node that tail's next pointer is connected to. Note that pos is not passed
as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
"""


# Definition for singly-linked list node (provided by LeetCode)
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Approach to solve the problem: Floyd's Cycle Detection Algorithm (Tortoise and Hare)
"""
ALGORITHM EXPLANATION:
================================================================
The solution uses Floyd's Cycle Detection Algorithm, also known as the "Tortoise and Hare" algorithm.

Steps:
1. Use two pointers: slow (tortoise) and fast (hare)
2. Move slow pointer one step at a time
3. Move fast pointer two steps at a time
4. If there's a cycle, the fast pointer will eventually meet the slow pointer
5. If there's no cycle, the fast pointer will reach the end (None)

Why this works:
- If there's no cycle: fast pointer reaches end first
- If there's a cycle: fast pointer moves twice as fast as slow pointer
- In a cycle, the fast pointer will "lap" the slow pointer and they'll meet

Time Complexity: O(n) - we visit each node at most once
Space Complexity: O(1) - only using two pointers, no extra space

Learning: 
1. Two-pointer technique is powerful for linked list problems
2. Floyd's algorithm is the standard approach for cycle detection
3. When fast pointer moves 2x speed of slow pointer in a cycle, they will always meet
4. This technique can be applied to other problems like finding cycle start position
"""


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # Edge case: if list is empty or has only one node without cycle
        if not head or not head.next:
            return False

        # Initialize two pointers
        slow = head  # Tortoise: moves 1 step at a time
        fast = head  # Hare: moves 2 steps at a time

        # Continue until fast pointer reaches end or finds cycle
        while fast and fast.next:
            # Move slow pointer one step
            slow = slow.next

            # Move fast pointer two steps
            fast = fast.next.next

            # If pointers meet, there's a cycle
            if slow == fast:
                return True

        # If we reach here, fast pointer hit the end, so no cycle
        return False


# Example walkthrough:
"""
Let's trace through the example: [3,2,0,-4] with pos=1 (cycle back to node with value 2)

Linked List: 3 -> 2 -> 0 -> -4
                  ^           |
                  |___________|

Initial: slow = 3, fast = 3

Step 1: 
- slow moves to 2 (slow = node with value 2)
- fast moves to 0 (fast = node with value 0)
- slow != fast, continue

Step 2:
- slow moves to 0 (slow = node with value 0)  
- fast moves to 2 (fast = node with value 2, due to cycle)
- slow != fast, continue

Step 3:
- slow moves to -4 (slow = node with value -4)
- fast moves to -4 (fast = node with value -4)
- slow == fast, return True (cycle detected!)

For a list without cycle like [1,2,3,4,5]:
- fast will reach None before meeting slow
- Return False (no cycle)
"""