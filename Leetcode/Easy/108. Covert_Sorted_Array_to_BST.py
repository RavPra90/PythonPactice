"""
LEETCODE PROBLEM: 108. Convert Sorted Array to Binary Search Tree
========================================
Problem Statement:
Given an integer array nums where the elements are sorted in ascending order,
convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees
of every node never differs by more than 1.

Example:
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted.

Input: nums = [1,3]
Output: [3,1] or [1,3]
"""

# Approach to solve the problem
"""
ALGORITHM EXPLANATION:
================================================================
Steps:
1. Use the middle element of the sorted array as the root (ensures balance)
2. Recursively build left subtree using left half of array
3. Recursively build right subtree using right half of array
4. Base case: if array segment is empty, return None

Key Insight: Since array is sorted, middle element ensures:
- All elements to the left are smaller (perfect for left subtree)
- All elements to the right are larger (perfect for right subtree)
- Tree remains height-balanced because we always split in half

Learning:
- Divide and conquer approach is perfect for balanced tree construction
- Middle element selection ensures height balance automatically
- Recursion naturally handles tree building from sorted data
- Time complexity: O(n) - visit each element once
- Space complexity: O(log n) - recursion stack depth for balanced tree
- This pattern applies to many "balanced structure from sorted data" problems
"""


# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sortedArrayToBST(nums):
    """
    Convert sorted array to height-balanced BST.

    Args:
        nums: List of integers in sorted ascending order

    Returns:
        TreeNode: Root of the constructed BST
    """

    def buildBST(left, right):
        """
        Helper function to build BST from array segment [left, right].

        Args:
            left: Left boundary index (inclusive)
            right: Right boundary index (inclusive)

        Returns:
            TreeNode: Root of BST for this segment, or None if segment is empty
        """

        # Base case: empty segment
        if left > right:
            return None

        # Find middle index - this will be our root
        # Using (left + right) // 2 ensures we get the left-middle for even-length arrays
        # This creates consistent tree structure
        mid = (left + right) // 2

        # Create root node with middle element
        root = TreeNode(nums[mid])

        # Recursively build left subtree from left half [left, mid-1]
        # All elements in this range are smaller than root
        root.left = buildBST(left, mid - 1)

        # Recursively build right subtree from right half [mid+1, right]
        # All elements in this range are larger than root
        root.right = buildBST(mid + 1, right)

        return root

    # Start building BST with entire array
    return buildBST(0, len(nums) - 1)


"""
DETAILED WALKTHROUGH EXAMPLE:
========================================
Let's trace through: nums = [-10, -3, 0, 5, 9]

CALL 1: buildBST(0, 4) - Process entire array [-10, -3, 0, 5, 9]
- left=0, right=4
- mid = (0+4)//2 = 2
- root = TreeNode(nums[2]) = TreeNode(0)
- Build left subtree: buildBST(0, 1) for [-10, -3]
- Build right subtree: buildBST(3, 4) for [5, 9]

CALL 2: buildBST(0, 1) - Process left half [-10, -3]
- left=0, right=1
- mid = (0+1)//2 = 0
- root = TreeNode(nums[0]) = TreeNode(-10)
- Build left subtree: buildBST(0, -1) → None (empty)
- Build right subtree: buildBST(1, 1) for [-3]

CALL 3: buildBST(1, 1) - Process single element [-3]
- left=1, right=1
- mid = (1+1)//2 = 1
- root = TreeNode(nums[1]) = TreeNode(-3)
- Build left subtree: buildBST(1, 0) → None (empty)
- Build right subtree: buildBST(2, 1) → None (empty)
- Return TreeNode(-3)

CALL 4: buildBST(3, 4) - Process right half [5, 9]
- left=3, right=4
- mid = (3+4)//2 = 3
- root = TreeNode(nums[3]) = TreeNode(5)
- Build left subtree: buildBST(3, 2) → None (empty)
- Build right subtree: buildBST(4, 4) for [9]

CALL 5: buildBST(4, 4) - Process single element [9]
- left=4, right=4
- mid = (4+4)//2 = 4
- root = TreeNode(nums[4]) = TreeNode(9)
- Build left subtree: buildBST(4, 3) → None (empty)
- Build right subtree: buildBST(5, 4) → None (empty)
- Return TreeNode(9)

FINAL TREE STRUCTURE:
       0
      / \
   -10   5
     \    \
     -3    9

Tree Properties Verification:
- Height balanced: ✅ (all leaf nodes are at depth 2-3, difference ≤ 1)
- BST property: ✅ (left < root < right for all nodes)
- All original elements included: ✅

========================================
Another Example: nums = [1, 2, 3, 4, 5, 6, 7]

PROCESS:
- Root: nums[3] = 4 (middle of 7 elements)
- Left subtree from [1,2,3]: root = 2, left = 1, right = 3
- Right subtree from [5,6,7]: root = 6, left = 5, right = 7

RESULT:
       4
      / \
     2   6
    / \ / \
   1  3 5  7

Perfect balance achieved!
"""


# Helper function to print tree (for testing purposes)
def printInOrder(root):
    """Print tree in in-order traversal to verify BST property"""
    if root:
        printInOrder(root.left)
        print(root.val, end=" ")
        printInOrder(root.right)


# Test the solution
if __name__ == "__main__":
    # Test case 1
    nums1 = [-10, -3, 0, 5, 9]
    bst1 = sortedArrayToBST(nums1)
    # In-order traversal should give original sorted array

    # Test case 2
    nums2 = [1, 3]
    bst2 = sortedArrayToBST(nums2)

    # Test case 3 - single element
    nums3 = [0]
    bst3 = sortedArrayToBST(nums3)

    # Test case 4 - empty array
    nums4 = []
    bst4 = sortedArrayToBST(nums4)  # Should return None